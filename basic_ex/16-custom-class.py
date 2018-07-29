# -*- coding:utf-8 -*-

class Student(object):
  def __init__(self, name):
    self.name = name
  
  def __str__(self):
    return 'Student object(name:%s)' % self.name

  __repr__ = __str__

print Student('Ajioy')


class Fib(object):
  def __init__(self):
    self.a, self.b = 0, 1

  def __iter__(self):
    return self

  def next(self):
    self.a, self.b = self.b, self.a + self.b
    if self.a > 100000:
      raise StopIteration()
    return self.a

for n in Fib():
  print n

class Fib(object):
  def __getitem__(self, n):
    a, b = 1, 1
    for x in range(n):
      a, b = b, a + b
    return a

f = Fib()
print f[0]
print f[1]
print f[2]

print range(100)[5:10]

class Fib(object):
  def __getitem__(self, n):
    if isinstance(n ,int):
      a, b = 1, 1
      for x in range(n):
        a, b = b, a + b
      return a

    if isinstance(n, slice):
      start = n.start
      stop = n.stop
      a, b = 1, 1
      L = []
      for x in range(stop):
        if x >= start:
          L.append(a)
        a, b = b, a+b
      return L


f = Fib()
print f[0:5]
print f[:10]


print '*' * 20
class Student(object):
  def __init__(self):
    self.name = 'AJIOY'

s = Student()
print s.name
# print s.score # AttributeError

class Student(object):
  def __init__(self):
    self.name = 'Ajioy'
  
  def __getattr__(self, attr):
    if attr == 'score':
      return 99
    elif attr == 'age':
      return lambda:25
    raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print s.score
print s.age
print s.age()

# print s.lookup()

class Chain(object):

  def __init__(self, path=''):
    self._path = path

  def __getattr__(self, path):
    return Chain('%s/%s' % (self._path, path))

  def __str__(self):
    return self._path

print Chain().status.user.timeline.list

class Student(object):
  def __init__(self, name):
    self.name = name

  def __call__(self):
    print('My name is %s' % self.name)

  #def __call__(self, name):
  #  print('My name is %s' % name)

s = Student('Ajioy')
s()
#s('ajioy')

print callable([1,2,3])
print callable(max)
print callable(Student)
print callable(Student())


print '*' * 20
# 以下两个类不是同一个类，不同于ruby的打开类
class A(object):
  def run(self):
    print 'running...'

a = A()
a.run()
class A(object):
  def fly(self):
    print 'flying...'
a = A()
a.fly()
# a.run() # error
