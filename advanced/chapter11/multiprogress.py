# 多进程
# 对于CPU密集型操作，多线程无法做到并行操作，需要多进程编程
# 对于IO密集型操作，使用多线程，因为进程间切换的代价高于线程
# 1.耗费CPU的操作，数学计算、图形计算，多进程优于多线程
# 2.IO操作，多线程优于多进程

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor

# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# if __name__ == "__main__":
#     #with ThreadPoolExecutor(3) as executor: # 多线程
#     with ProcessPoolExecutor(3) as executor: # 多进程
#         all_task = [executor.submit(fib, (num)) for num in range(25,40)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#             print("result:{}".format(data))
#
#         print("last time is :{}".format(time.time() - start_time))
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
     with ThreadPoolExecutor(3) as executor: # 多进程
         all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
         start_time = time.time()
         for future in as_completed(all_task):
             data = future.result()
             print("result:{}".format(data))

         print("last time is :{}".format(time.time() - start_time))
