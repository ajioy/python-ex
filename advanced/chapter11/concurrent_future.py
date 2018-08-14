
# 为什么要用线程池
# 1.提供了数量控制
# 2.可以获取某一个线程的状态及返回值
# 3.当一个线程完成的时候,主线程能够立马知道它的状态
# 4.futures可以让多线程和多进程编码接口一致

#from concurrent import futures # 多进程\多线程变得相对容易
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future

# Future贯穿于整个异步编程
# 未来对象,task的返回容器，任务的执行结果或状态

import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times



executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中
# submit是非阻塞的，会立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))

# 获取已经成功的task任务
urls = [3,2,4] # 虽然线程池里只有2个worker，但是可以提交任意个任务进来
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task) # 等待所有任务执行完成才执行下一步
# wait(all_task, return_when=FIRST_COMPLETED)
print("main done")
# as_completed是生成器，它找出所有已完成的任务
# 一旦异步任务完成，主线程立马能收到
# for future in as_completed(all_task):
#     data = future.result() # 获取线程返回值
#     print("get {} page".format(data))

# 通过executor的map获取已经完成的task值
# 以下执行的顺序是和urls列表的顺序一致
# for data in executor.map(get_html, urls): # 将urls里的元素一一放至get_html处理
#     print("get {} page".format(data))


# print(task1.done()) # 判定任务是否执行成功
# print(task2.cancel()) # 在没开始执行前取消一个任务，如果已经执行中或已经执行完成会失败
# time.sleep(4)
# print(task1.done()) # 执行成功
# # 阻塞的方法，可以获取task的执行结果
# print(task1.result())


