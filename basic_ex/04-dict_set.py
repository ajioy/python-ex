#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
d = {'Ajioy': 95, 'Bob': 92, 'Cheer': 23}
print d['Ajioy']
d['Bob'] = 88
print d
print 'Hello' in d # False
print d.get('Ajioy')
print d.get('Hello') # none
print d.get('Hello', -1) # 默认值
print d.pop('Bob')
print d

s = set([1,2,3])
print s
s.add(4)
print s
s.remove(4)
print s
s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2
print s1 | s2
