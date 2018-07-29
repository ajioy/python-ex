# -*- coding: utf-8 -*-
#  切片
L = ['Ajioy', 'Bob', 'Cheer', 'Duck', 'Effect']
print L[0:3] # 取前三个元素，0,1,2，不包括3
print L[:3] # 等价于L[0:3]
print L[1:3]
print L[-2:] # 倒数第二个开始取到结尾

M = range(100)
print M[:10] # 0..9
print M[1:11] # 1..10
print M[-10:] # 最后10个元素，90..99
print M[:10:2] # 前10个元素，每隔2个取1次
print M[::5] # 所有数，每隔5个取1次
print M[:] # 复制一份
print 'ABCDEFG'[1:3]
print 'ABCDEFG'[::2]

# 迭代
from collections import Iterable
print isinstance('abc', Iterable)
print isinstance([1,2,3], Iterable)
print isinstance(123, Iterable)

for i, value in enumerate(['a','b','c','d']):
  print i,value

for x,y in [(1, 1), (2, 4), (3, 9)]:
  print x, y

# 列表生成器
print range(1,11)
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]
print [m + n for m in 'ABC' for n in 'XYZ']

d = {'x': 'A', 'y': 'B', 'z' : 'C'}
for k, v in d.iteritems():
  print k, '=', v

print [k + '=' + v for k, v in d.iteritems()]
print [s.lower() for s in L]
L = ['adfas', 'gdsfs', 1231, 'fdsd', 1.231, True, False]
print [s.lower() for s in L if isinstance(s, str)]

# 生成器
L = [ x * x for x in range(1, 11)] # list
print L
g = (x * x for x in range(1, 11)) # 生成器, 保存的算法
print g
print g.next() # 几乎不会调用
print g.next()

for n in  g:
  print n

def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print b, # 不换行
    a, b = b, a + b
    n = n + 1

fib(6)

print "\n generator"
def fib2(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1

f = fib2(6)
print f
print f.next()
print f.next()
print f.next()
for e in f:
  print e,
