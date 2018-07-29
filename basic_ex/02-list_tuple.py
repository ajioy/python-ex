# -*- coding:utf-8 -*-
classmates = ['Ajioy', 'Bob', 'Cheer']
print(classmates)
print(len(classmates))
print(classmates[0], classmates[1], classmates[2])
print("last:%s" % classmates[-1])
classmates.append('Nero')
print("After append %s" % classmates)
classmates.insert(1, 'Jack')
print("After insert %s" % classmates)
classmates.pop(1)
print("After pop %s" % classmates)
classmates[1] = "Sara"
print("After modify %s" % classmates)

L = ['Apple', 123, 12.0012, True]
print(L)
s = ["Python", "Ruby", ["django","flask","tornado"], "Golang"]
print s, len(s)
print s[2][2]

# tuple 不可变，指向的对象不可变
classmates = ("Ajioy", "Bob", "Clever")
print(classmates)
print(classmates[0])
t = (1,)
t1 = (1)
print(t, t1)
t2 = (1,2,3)
print(t2)
# t2[0] = 23
# print(t2) error

# 指向可变对象list，list本身没变，里面的元素变了而已
t3 = ('a', 'b', ['A', 'B'])
print(t3)
t3[2][0] = 'X'
t3[2][1] = 'Y'
print(t3)


