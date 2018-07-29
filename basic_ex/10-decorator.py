# -*- coding:utf-8 -*-
def now():
  print '2018-06-23'

f = now
f()

print now.__name__
print f.__name__

def log(func):
  def wrapper(*args, **kw):
    print 'call %s():' % func.__name__
    return func(*args, **kw)
  return wrapper

@log
def now2():
  print '2018-06-23'

now2()
print

def log2(func):
  def wrapper(*args, **kw):
    print 'call %s()' % func.__name__
    func(*args, **kw)
    print 'after call do something'
    return func(*args, **kw)
  return wrapper


@log2 # 相当于now = log(now)
def now3():
  print '2018-06-23'

now3()
print now3.__name__

def log3(text):
  def decorator(func):
    def wrapper(*args, **kw):
      print '%s, %s():' % (text, func.__name__)
      return func(*args, **kw)
    return wrapper
  return decorator

@log3('excute') # 相当于now = log('excute')(now)
def now4():
  print '2018-06-24'

print
now4()
print now4.__name__ # wrapper

import functools

def log4(func):
  @functools.wraps(func) # 将wrapper.__name = func.__name__
  def wrapper(*args, **kw):
    print 'call %s():' % func.__name__
    return func(*args, **kw)
  return wrapper


@log4
def now5():
  print '2018-06-24'

now5()
print now5.__name__

def log5(text):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
      print 'call %s %s()' % (text, func.__name__)
      return func(*args, **kw)
    return wrapper
  return decorator

@log5("excute")
def now6():
  print '2018-06-24'

now6()
print now6.__name__


print int('123456')
print int('123456', base=8)
print int('123456', 16)
print int('100', 2)


#def int2(x, base=2):
#  return int(x, base)

int2 = functools.partial(int , base = 2)
print int2('100010')
