#!/usr/bin/env python
#-*- coding: utf-8 -*-

from socket import socket,AF_INET,SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 80))
print 'Bind UDP on 80'
while True:
  data, addr = s.recvfrom(1024)
  print 'Received from %s:%s.' % addr
  s.sendto('Hello, %s' % data, addr)

