#!/usr/bin/env python
#-*- coding: utf-8 -*-

from socket import socket,AF_INET,SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
addr = ('127.0.0.1', 80)
for data in ['Ajioy', 'Bob', 'Cheer']:
  s.sendto(data, addr)
  print s.recv(1024)

s.close()
