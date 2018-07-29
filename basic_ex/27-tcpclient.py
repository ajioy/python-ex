#!/usr/bin/env python
#-*- coding: utf-8 -*-

from socket import socket,AF_INET,SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 80))
print s.recv(1024)
names = ['Ajioy', 'Bob', 'Clear','exit', 'Dallor']
for data in names:
  s.send(data)
  data = s.recv(1024)
  if data:
    print data
  else:
    break

s.close()
print 'all over'

