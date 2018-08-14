import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    sock.send(b"Welcome to server!")
    while True:
        data = sock.recv(1024) # 注意，这里不能写socket.recv
        if not data or data.decode("utf8") == "exit":
            break

        print("client:{}say:\n{}\n".format(addr,data.decode("utf8")))
        sock.send("Hello,{}!You are goodboy!\n".format(addr).encode("utf8"))

    sock.send("Goodbye,{}\n".format(addr).encode("utf8"))
    sock.close()
    print("{} disconnected!\n".format(addr))


while True:
    sock, addr = server.accept()
    # 要用多线程实现多用户连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()




