# -*- coding:utf-8 -*-
class Student(object):

  def get_score(self):
    return self._score

  def set_score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 and 100')
    self._score = value


s = Student()
s.set_score(10)
print s.get_score()
# s.set_score(1000) # error

class StudentEx(object):

  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 and 100')
    self._score = value

  @property
  def birth(self):
    return self._birth

  @birth.setter
  def birth(self, value):
    self._birth = value

  @property # readonly
  def age(self):
    return 2018-self._birth

s = StudentEx()
s.score = 99
print s.score

s.birth = 1990
print s.birth
print s.age
# s.age = 100 #error
