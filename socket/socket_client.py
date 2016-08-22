#-*- coding=utf-8 -*-
__author__ = 'ajioy'
__create_data__ = '2016/8/22 12:50'
__py_version__ = '2.7.8'
__description__ = ''

import socket

skclient = socket.socket()
ip_port = ('127.0.0.1', 9999)
skclient.connect(ip_port)

while True:
    data = skclient.recv(1024) #接收服务器端发来的数据
    print data
    senddata = raw_input("client:")
    skclient.send(senddata)
    if (senddata == 'end'):
        break

skclient.close()