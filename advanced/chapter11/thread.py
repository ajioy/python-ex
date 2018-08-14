# 进程对内在消耗较大
# 对于IO操作,多线程和多进程差别不大
import time
import threading

# 方式一，函数调用形式，此方法适用于简单的逻辑
def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")

    # 方式二：通过继承Thread来实现多线程
    # 大部分情况下，此方法更为适用
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")

if __name__ == "__main__":
    start_time = time.time()
    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    #thread1.setDaemon(True) # 将线程设为守护线程，当主线程结束时，守护进程也随之关闭掉
    #thread2.setDaemon(True)
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    thread1.start()
    thread2.start()
    # 阻塞住，直接线程结束后才继续运行主线程，这个时候设置的setDaemon就不生效了
    thread1.join()
    thread2.join()

    print("last time:%f" % (time.time() - start_time))

