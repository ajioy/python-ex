import socket

cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_socket.connect(('127.0.0.1', 8000))

while True:
    data = cli_socket.recv(1024).decode("utf8")
    print("Server say:%s\n" % data)
    raw_data = input("Client say:\n")
    if "exit" in raw_data:
        break
    cli_socket.send(raw_data.encode("utf8"))

cli_socket.close()
print("Disconnected from server!\n")

