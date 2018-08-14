# asyncio爬虫、去重、入库
import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery


stopping = False
start_url = "http://python.jobbole.com/"
waitting_urls = []
seen_urls = set()

sem = asyncio.Semaphore(3)

async def fetch(url, session):
    async with sem:
        #await asyncio.sleep(1)
        try:
            async with session.get(url) as rsp:
                print('url status: {}'.format(rsp.status))
                if rsp.status in [200, 201]:
                    print(await rsp.text())
                    data = await rsp.text()
                    return data
        except Exception as e:
                    print(e)

# 解析是cpu完成的,不耗费IO
def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


# 获取文章详情并解析入库
async def article_handle(url, session, pool):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("select 42;")
            insert_sql = "insert into article(title) values('{}')".format(title)
            await cur.execute(insert_sql)
            # print(cur.description)
            # (r,) = await cur.fetchone()
            # assert r == 42


# 不停地取数据
async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue

            url = waitting_urls.pop()
            print("start ")
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handle(url, session, pool))
                    await asyncio.sleep(0.5)
            # else:
            #     if url not in seen_urls:
            #         asyncio.ensure_future(init_urls(url, session))



async def main(loop):
    #global pool
    # 等待mysql连接好
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='zhjie1207',
                                      db='aiomysql_test', loop=loop,
                                      charset="utf8", autocommit=True) # 这两个是坑，要注意

    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)

    asyncio.ensure_future(consumer(pool)) # 不停地从URL中取数据

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()