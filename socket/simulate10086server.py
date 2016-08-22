#-*- coding=utf-8 -*-
__author__ = 'ajioy'
__create_data__ = '2016/8/22 15:48'
__py_version__ = '2.7.8'
__description__ = ''

import socket
import random

def printSomething(conn):
    conn.send("Fool")

def testIQ(conn):
    conn.send("your IQ is:%d" % random.randint(65,120))

def sendJoke(conn):
    conn.send("ok, u are a joke!...GET OUT HERE!STUPID FOOL!...")

switch = {
    1:printSomething,
    2:testIQ,
    3:sendJoke
}
under = 1
upper = 3

sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen(10)

while True:
    conn, addr = sk.accept()
    conn.send("hello,my dear:\n" \
             +"what can i do for u:?\n"
             +"\t1:print your address\n"
              +"\t2:test your IQ\n"
              +"\t3:send u a joke\n")
    flag = True
    while flag:
        recvdata = conn.recv(1024)
        case = int(recvdata)
        if case >= under and case <= upper:
            switch[case](conn)
        elif recvdata == 'end':
            flag = False
        else:
            conn.send("error input!try again!(only 1-3)")
        # if recvdata == '1':
        #     printSomething(conn)
        # elif recvdata == '2':
        #     testIQ(conn)
        # elif recvdata == '3':
        #     sendJoke(conn)
        # elif recvdata == 'end':
        #     flag = False
        #     conn.close()
        # else:
        #     conn.send("error input!try again!(only 1-3)")
    conn.close()

sk.close()

