#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: 19-debug.py
# Author: Ajioy
# mail: ajioy@hotmail.com

def foo(s):
  n = int(s)
  #print '>>> n = %d' % n
  assert n != 0, 'n is zero!'
  return 10 / n

def main():
  print foo('0')

#main()


import logging
logging.basicConfig(level=logging.DEBUG)
import pdb

s = '0'
n = int(s)
pdb.set_trace()
logging.info('n = %d' % n)
print 10 / n
