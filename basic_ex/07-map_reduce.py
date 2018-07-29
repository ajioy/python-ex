# -*- coding:utf-8 -*-
f = abs
print f
print f(-20)

def add(x, y, f):
  return f(x) + f(y)

print add(-12, -1, abs)


# map
def func(x):
  return x * x

print map(func, [1,2,3,4,5,6,7,8,9])
print map(str, range(10))


def add2(x, y):
  return x + y

print reduce(add2, [1, 3, 5, 7, 9])

def fn(x, y):
  return x * 10 + y

print reduce(fn, [1, 3, 5, 7, 9])

# 还可以这样玩，函数定义里嵌套定义函数并调用
def str2int(s):
  print "in str2int"
  def fn(x, y):
    print "in fn %d" % (x * 10 + y)
    return x * 10 + y
  def char2num(s):
    print("in char2num %s" % s)
    return {'0':0,  '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
  print "reduce"
  return reduce(fn, map(char2num, s))


#print str2int(['1','3','5'])
print str2int('12345')


def char2num(s):
  return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int_v2(s):
  return reduce(lambda x,y: x * 10 + y, map(char2num, s))

print str2int_v2('54321')

def fix(s):
  return s[0].upper() + s[1:].lower()
input = ['adam', 'LISA', 'barT']
print map(fix, input)
print map(lambda x:x[0].upper() + x[1:].lower(), input)
print map(lambda x:x.lower().title(), input)
