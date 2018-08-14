# 通过queue的方式进行线程间通信

import time
import threading
from queue import Queue

def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        if len(queue):
            url = queue.get() # 阻塞的方法，线程安全的
            print(url)
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")



def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            # queue.put是线程安全的
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize = 1000)
    start_time = time.time()
    thread1 = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(5):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()


    thread1.start()
    detail_url_queue.task_done() # 和join成队出现
    detail_url_queue.join()

    print("last time:%f" % (time.time() - start_time))
