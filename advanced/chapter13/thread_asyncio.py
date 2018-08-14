# 协程使用多线程：在协程中集成阻塞IO
import asyncio
from concurrent.futures import ThreadPoolExecutor
import socket
from urllib.parse import urlparse
import time

# 阻塞接口，结合asyncio使用
# 通过socket请求html
def get_url(url):
    url = urlparse(url)
    host = url.netloc # host
    path = url.path
    if path == "":
        path = "/"


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    # http协议
    # \r\n 换行符
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(\
        path, host).encode("utf8"))
    buffer = []
    # 读完所有数据
    while True:
        d = client.recv(1024)
        if d:
            buffer.append(d)
        else:
            break

    data = b''.join(buffer).decode("utf8") # 取决于各个网站
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    # 协程里最好不要调用阻塞IO函数
    # 如果一定要用，把阻塞代码放到线程池中运行
    loop = asyncio.get_event_loop()
    start_time = time.time()
    # 线程池
    executor = ThreadPoolExecutor(3)
    tasks = []
    for url in range(20):
        url = "http://blog.csdn.net/ajioy"
        # 将阻塞IO函数放在以下函数中运行
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time() - start_time)
