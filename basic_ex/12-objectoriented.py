# -*- coding:utf-8 -*-
class Student(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def print_score(self):
    print '%s, %s' % (self.name, self.score)

  def get_grade(self):
    if self.score >= 90:
      return 'A'
    elif self.score >= 60:
      return 'B'
    else:
      return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

bart.name = 'Bart Ajioy'
print bart.name
bart.print_score()
print bart.get_grade()
print lisa.get_grade()

bart.age = 100
print bart.age


# print lisa.age # error

class Student2(object):
  def __init__(self, name, score):
    self.__name = name
    self.__score = score

  def print_score(self):
    print '%s : %s' % (self.__name, self.__score)

  def get_name(self):
    return self.__name

  def get_score(self):
    return self.__score

  def set_score(self, score):
    if 0 <= score <= 100:
      self.__score = score
    else:
      raise ValueError('bad error')

ajioy = Student2('Ajioy Scotte', 98)
# print ajioy.__name # error
ajioy.print_score()

print ajioy.get_name()
# ajioy.set_score(101)
print ajioy._Student2__name

print '*' * 20

class Animal(object):
  def run(self):
    print 'Animal is running...'

class Dog(Animal):
  pass

class Cat(Animal):
  pass

dog = Dog()
dog.run()
cat = Cat()
cat.run()

class Dog(Animal):
  def run(self):
    print 'Dog is running...'

  def eat(self):
    print 'Eating meat...'

dog2 = Dog()
dog2.run()
dog2.eat()

class Cat(Animal):
  def run(self):
    print 'Cat is running...'

cat2 = Cat()
cat2.run()

print isinstance(cat, Animal)
print type(cat)
print isinstance(cat2, Cat)
print isinstance(dog, Animal)
print isinstance(dog2, Dog)


def run_twice(animal):
  animal.run()
  animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
  def run(self):
    print 'Tortoise is running slowly...'

run_twice(Tortoise())


print '*' * 20
print type(123)
print type('abc')
print type(123.312)
print type([1,3,2])
print type([1,3.23,'123'])
print type({'a':'b', 'b':'c'})
print type(None)
print type(True)
print type(False)
print type(dog)

print type(abs)

import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(int) == types.TypeType

print dir('ABC')
# print dir(int)
print len('ABC')
print 'ABC'.__len__()

class MyObject(object):
  def __init__(self):
    self.x = 9

  def power(self):
    return self.x * self.x

  def __len__(self):
    return 100

obj = MyObject()
print len(obj)
print hasattr(obj, 'x') # true
print hasattr(obj, 'y') # false

setattr(obj, 'y', 19)
print obj.y

print getattr(obj, 'z', 404)
