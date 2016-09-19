# -*- coding:utf-8 -*-
__author__ = 'AjioyHome'
__date__ = '16-7-31 下午9:43'
__description__ = 'list and tuple exercise '

L2 = ['ajioy','christan', 'azao', 'leihaipeng', 1, 2]
print L2,len(L2)
L2[2] = 'pinger'
print L2
L2.pop(0)
print L2
L2.insert(0,'ajioy')
print L2
L2.insert(-1, [3,4,5])
print L2
L2.append('the last one,the end')
print L2

tuple = 1,2,'ajioy'
print tuple

te = ()
print te\

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print L[0][0],L[1][2],L[2][2]

a = 'abc'
print a
b = a.replace('a','A')
print a,b

s = set([1,2,3])
print s