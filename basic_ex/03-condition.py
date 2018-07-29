#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
age = 28
if age >= 18:
  print('your age is', age)
  print('adult')
elif age >= 6:
  print('teenager')
else:
  print('kid')


names = ['Ajioy', 'Bob', 'Cheer']
for name in names:
  print(name)

sum = 0
for x in [1, 2, 3, 4]:
  sum += x
print(sum)

sum = 0
for x in range(101): # 0..100
  sum += x
print(sum)

sum = 0
n = 99
while n >0:
  sum += n
  n = n - 2

print(sum)

birth = int(raw_input('birth:'))
if birth < 2000:
  print(u'00前')
else:
  print(u'00后')
