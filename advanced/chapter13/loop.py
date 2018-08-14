# 高并发编程模式中具备的三个要素:
# 协程三要素：
# 事件循环，回调(驱动生成器)，epoll（IO多路复用）

# asyncio是python自带的，用于解决异步io编程的一整套解决方案
# tornado、gevent、twisted(scrapy, django channels)
# tornado协程+事件循环的形式完成高并发、实现web服务器
# django + falsk 阻塞IO编程模型，不带web服务器（socket编码）uwsgi, gunicorn+nginx
# tornado可以直接部署，nginx+tornado

# 使用asyncio
import asyncio
import time
from functools import partial # 将函数包装成另一个函数

async def get_html(url):
    print("start get url")
    # time.sleep(10) # 同步阻塞接口，不能使用，否则每次调用都会阻塞2秒,10次就20秒
    # await time.sleep(2) # 报错，await后面必须跟一个AWaitable对象
    await asyncio.sleep(2) # 要加await，否则无效且报异常，多个协程(哪怕1000个）执行不会阻塞超过2秒
    print("end get url")
    return "ajioy"

# 定义接收参数的时候，必须放在前面
def callback(url,future):
    print("send email to ajioy")
    print("url:%s" % url)

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    #loop.create_task()
    # tasks = [get_html("blog.csdn.net/ajioy") for i in range(1000)]
    # 以下可简单地理解为thread.join方法，它会等待协程执行完毕
    # loop.run_until_complete(get_html("http://blog.csdn.net/ajioy"))
    # loop.run_until_complete(asyncio.wait(tasks)) # 2秒左右完成所有请求
    # 注册协程到loop队列中，一个线程只有一个loop，内部调用
    # get_future = asyncio.ensure_future(get_html("http://blog.csdn.net/ajioy"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())
    # task是Future类的子类
    # 将协程注册到loop当中
    # task = loop.create_task(get_html("http://blog.csdn.net/ajioy"))
    # # 执行完上面的任务后，会调用下面的回调函数
    # #task.add_done_callback(callback)
    # task.add_done_callback(partial(callback, "http://blog.csdn.net/ajioy"))
    # loop.run_until_complete(task)
    # print(task.result())
    # tasks = [get_html("blog.csdn.net/ajioy") for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*tasks))
    '''
    # gather和wait的区别
    # gather比wait更加高级抽象
    '''
    groups1= [get_html("blog.csdn.net/ajioy") for i in range(10)]
    groups2= [get_html("blog.csdn.net/scotte") for i in range(10)]
    groups1 = asyncio.gather(*groups1)
    groups2 = asyncio.gather(*groups2)
    groups2.cancle() # 批量取消任务
    loop.run_until_complete(asyncio.gather(groups1, groups2))
    #loop.run_until_complete(asyncio.gather(*groups1, *groups2))
    print(time.time() - start_time)
