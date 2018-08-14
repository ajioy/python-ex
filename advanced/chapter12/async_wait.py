# python为了将语义变得更加明确，引入了async和await关键词
# 用于定义原生的协程,区别于生成器
# 生成器的原理实现的协程
# async def downloader(url):
#     return "ajioy"
import types

@types.coroutine  # AWaitable对象
def downloader(url):
    yield "ajioy"

# async修饰的函数里只能用await，不能用yield和yield from
async def download_url(url):
    # dosomething
    html = await downloader(url) # 可以理解为yield from

    return html

if __name__ == "__main__":
    coro = download_url("blog.csdn.net/ajioy")
    # next(None)
    value = coro.send(None)
    print(value)