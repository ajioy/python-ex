# select完成http请求

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# DefaultSelector

selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False
class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format( \
                        self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)


    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd) # 确定读完了数据
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc # host
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


# 判定哪一个可读可写
# 1.select本身不支持register模式
# 2.socket状态变化以后的回调是由程序员完成的
# 事件循环，不停地请求socket的状态并调用对应用的回调函数
# 回调+事件循环+select(poll\epoll)，经典模式 tornado, gevent
# 好处：并发性高，使用单线程，成千上万个连接没问题
def loop():

    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == "__main__":
    import time
    start_time = time.time()
    for i in range(20):
        fetcher = Fetcher()
        fetcher.get_url("http://www.baidu.com")

    loop()
    print(time.time() - start_time)


