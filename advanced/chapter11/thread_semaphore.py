# Semaphore用于控制进入数量的锁
# 文件读写问题，写用一个线程，读用多个线程

import threading
import time

class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()


# 希望一次并发3个
class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire() # 每调一次会减1
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()