# -*- coding:utf-8 -*-
def is_odd(n):
  return n % 2 == 1

print filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15])

def not_empty(s):
  return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

def reversed_comp(x,y):
  if x > y:
    return -1
  if x < y:
    return 1
  return 0

print sorted([231, 321, 32, 453])
print sorted([231, 321, 32, 453], reversed_comp)

def cmp_ignore_case(s1, s2):
  u1 = s1.upper()
  u2 = s2.upper()
  if u1 < u2:
    return -1
  if u1 > u2:
    return 1
  return 0

print sorted(['Bob', 'Ajioy', 'crazy', 'about'], cmp_ignore_case)
