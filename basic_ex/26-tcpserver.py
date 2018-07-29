#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import socket
from socket import *
import time
import threading

def tcplink(sock, addr):
  print 'connected from %s:%s' % addr
  sock.send('Welcome to server!')
  while True:
    data = sock.recv(1024)
    time.sleep(1)
    if not data or data == 'exit':
      break
    sock.send('Hello, dear %s!' % data)

  sock.close()
  print 'closed connection %s:%s' % addr

def test():
  s = socket(AF_INET, SOCK_STREAM)
  s.bind(('127.0.0.1', 80))
  s.listen(5)
  print 'waiting for connecting...'
  while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

  s.close()

if __name__ == '__main__':
  test()
