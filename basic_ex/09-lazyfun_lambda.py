# -*- coding:utf-8 -*-
def calc_sum(*args):
  ax = 0
  for n in args:
    ax = ax + n
  return ax

def lazy_sum(*args):
  def sum():
    ax = 0
    for n in args:
      ax = ax + n
    return ax
  return sum

f = lazy_sum(1, 3, 5, 7, 9)
print f

print f()

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2 # false

def count():
  fs = []
  for i in range(1, 4):
    def f():
      return i * i
    fs.append(f)
  return fs

# 返回的函数引用了变量i，但它并非立刻执行
f1, f2, f3 = count()
print f1(), f2(), f3() # 9, 9, 9

def count2():
  fs = []
  for i in range(1, 4):
    def f(j):
      def g():
        return j * j
      return g
    fs.append(f(i))
  return fs

f1, f2, f3 = count2()
print f1(), f2(), f3() # 1, 4, 9


def count3():
  fs = []
  for i in range(1, 4):
    fs.append(lambda j = i:j * j)
  return fs

f1, f2, f3 = count3()
print f1(), f2(), f3()

# lambda
print map(lambda x: x * x, [1,2,3,4,5,6,7,8,9])

f = lambda x: x * x
print f, f(10)

def build(x, y):
  return lambda: x * x + y * y

f = build(10, 20)
print f()

