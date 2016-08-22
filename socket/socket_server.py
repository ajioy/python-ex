#-*- coding=utf-8 -*-
__author__ = 'ajioy'
__create_data__ = '2016/8/22 12:44'
__pyversion__ = '2.7.8'
__description__ = ''

import socket

sk = socket.socket()
ip_port  = ('127.0.0.1', 9999)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn, addr = sk.accept() #who,where
    conn.send("hello,client:\nI'm the server, your god!\
    \nwhat you want?")

    flag = True
    while flag:
        recv_from_client = conn.recv(1024)
        print recv_from_client
        if(recv_from_client == 'end'):
            flag = False
            conn.close()
        conn.send("get out here!")

sk.close()