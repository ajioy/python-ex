import socket
from urllib.parse import urlparse

# 使用非阻塞IO完成HTTP请求
# 通过socket请求html
def get_url(url):
    url = urlparse(url)
    host = url.netloc # host
    path = url.path
    if path == "":
        path = "/"


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass


    # http协议
    # \r\n 换行符
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(\
                        path, host).encode("utf8"))
            break
        except OSError as e:
            pass

    buffer = []
    # 读完所有数据
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue

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