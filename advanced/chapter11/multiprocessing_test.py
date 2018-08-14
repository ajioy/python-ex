# import os
# import time
# # fork只能用于linux/unix中
# pid = os.fork()
# print("ajioy")
# if pid == 0:
#     print("子进程")
# else:
#     print("主进程")
#
# time.sleep(2)

# 以上两个结果都会打印出来
# 进程之间的数据是完全隔离的

import multiprocessing
import time

def get_html(n):
    time.sleep(n)
    print("sub progress success")
    return n

class MyProgress(multiprocessing.Process):
    def run(self):
        pass

if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid) # None
    # progress.start()
    # print(progress.pid) # 才存在
    # progress.join()
    # print("main progress end")

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    #
    # pool.close() # 一定要先调用此方法关闭进程池，否则join方法将会报错
    # pool.join() # 等待所有任务完成
    # print(result.get())

    # 任务完成顺序是和列表添加顺序一致
    for result in pool.imap(get_html, [1,5,3]):
        print("{} sleep success.".format(result))

    # 无序的，谁先完成谁先打印出来结果
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success.".format(result))
