# -*- coding:utf-8 -*-
class Student(object):
  pass

s = Student()
s.name = 'Ajioy'
print s.name

# 给一个实例绑定一个方法
def set_age(self, age):
  self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)
s.set_age(28)
print s.age

# 给实例绑定方法只对特定实例有效，对另一个实体是不起作用的
s2 = Student()
#s2.set_age(20)
#print s2.age # 给一个

# 给所有实例绑定方法用class
def set_score(self, score):
  self.score = score

Student.set_score = MethodType(set_score, None, Student)

s.set_score(100)
print s.score

s2.set_score(93)
print s2.score

# 限制class的属性
class StudentEx(object):
  __slots__ = ('name', 'age')

s = StudentEx()
s.name = 'Ajioy'
print s.name
s.age = 28
print s.age
#s.score = 90 # error
#print s.score

# 除非在子类中也定义__slots__，否则子类不受父类的限制
class GraduateStudent(Student):
  pass

s = GraduateStudent()
s.score = 100 # ok
print s.score
