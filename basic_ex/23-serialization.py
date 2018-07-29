#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
  import cPickle as pickle
except ImportError:
  import pickle

d = dict(name='Bob', age=20, score=88)
print d
print pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d

print '*' * 20

# JSON
import json
d = dict(name='ajioy', age=28, score=99)
print json.dumps(d)
print type(json.dumps(d)) # str

json_str = '{"age" : 20, "score" : 90, "name": "AJIOY"}'
print json.loads(json_str) # unicode, not str

# JSON Advanced
class Student(object):
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score

s = Student('Ajioy', 28, 99)
#print(json.dumps(s))


def student2dict(std):
  return {
      'name': std.name, 
      'age' : std.age,
      'score':std.score
      }

#print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
  return Student(d['name'], d['age'], d['score'])

json_str = '{"age" : 20, "score" : 90, "name": "AJIOY"}'
s = json.loads(json_str, object_hook=dict2student)
print s.name

