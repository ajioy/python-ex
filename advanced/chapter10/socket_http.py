# requests->基于urllib->基于socket

import socket
from urllib.parse import urlparse

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

    get_url("http://www.baidu.com")