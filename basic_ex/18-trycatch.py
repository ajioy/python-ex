#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: 18-trycatch.py
# Author: Ajioy
# mail: ajioy@hotmail.com

try:
  print 'try...'
  r = 10 / 0
  print 'result:', r
except ZeroDivisionError, e:
  print 'except:', e
finally:
  print 'finally...'
print 'END'


try:
  print 'try...'
  r = 10 / int('a')
  print 'result:', r
except ValueError, e:
  print 'ValueError:', e
except ZeroDivisionError, e:
  print 'ZeroDivisionError:', e
else:
  print 'no error'
finally:
  print 'finally...'
print 'END'

print '*' * 20
# 捕获其子类也会“一网打尽”
#try:
#  foo()
#except StandardError, e:
#  print 'StandardError'
#except ValueError, e:
#  print 'valueError'
def foo(s):
  return 10 / int(s)

def bar(s):
  return foo(s) * 2

def main():
  try:
    print bar('0')
  except StandardError, e:
    print 'Error!'
  finally:
    print 'finally...'

main()


def main():
  bar('0')

#main()


import logging

def foo(s):
  return 10 / int(s)

def bar(s):
  return foo(s) * 2

def main():
  try:
    bar('0')
  except StandardError, e:
    logging.exception(e)

main()
print 'End'

class FooError(StandardError):
  pass

def foo(s):
  n = int(s)
  if n == 0:
    raise FooError('invalid value:%s' % s)

  return 10 / n

#print foo('0')


def foo(s):
  n = int(s)
  return 10 / n

def bar(s):
  try:
    return foo(s) * 2
  except StandardError, e:
    print 'Error!'
    raise

bar('0')

