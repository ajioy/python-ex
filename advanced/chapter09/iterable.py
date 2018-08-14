# 什么是迭代协议
# 可迭代类型Iterable,迭代器Iterator
# 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性方式数据的方式
# 凡是可迭代的,都是实现了迭代协议,可以用for来循环迭代
# list只是可迭代类型(Iterable，实现__iter__),但区别于迭代器(Iterator要实现__next__方法)

from collections.abc import Iterable, Iterator
a = [1,2]
print(isinstance(a, Iterable)) # True
print(isinstance(a, Iterator)) # False

iter_rator = iter(a)
print(isinstance(iter_rator, Iterator)) # True
