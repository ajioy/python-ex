# asyncio不提供http协议的接口
# aiohttp
import asyncio
import socket
import time
from urllib.parse import urlparse

# 用协程同步的编程思想来编写高效的、异步的HTTP请求
async def get_url(url):
    url = urlparse(url)
    host = url.netloc # host
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接比较费时
    # 凡是有await的地方，协程都给返回了一个Future对象，是不用等待的
    # Future对协程来说很重要
    # 传统阻塞IO,只有等执行成功后才会返回结果

    reader, writer = await asyncio.open_connection(host, 80 )
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(\
        path, host).encode("utf8"))

    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf8")
        all_lines.append(data)

    html = "\n".join(all_lines)
    #print(html) # 打印结果方式一
    return html

async def main(loop):
    tasks = []
    for url in range(20):
        url = "http://www.baidu.com"
        tasks.append(asyncio.ensure_future(get_url(url)))

    # 打印结果方式三，获取到一个就打印出一个
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)



if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 打印结果方式二, 外部方式获取结果
    # tasks = []
    # for url in range(20):
    #     url = "http://www.baidu.com"
    #     tasks.append(asyncio.ensure_future(get_url(url)))
    # loop.run_until_complete(asyncio.wait(tasks))
    # for task in tasks:
    #     print(task.result())

    loop.run_until_complete(main(loop))
    print(time.time() - start_time)
