# python3.3新加yield from语法

from itertools import chain

my_list = [1,2,3]
my_dict = {
    "ajioy": "google",
    "ajioy1": "twitter",
}

# def g1(iterable): # 传进来怎么样,传出去怎么样
#     yield iterable
#
# def g2(iterable): # 传进来怎么样,传出去之前将其迭代
#     yield from iterable
#
# for value in g1(range(10)):
#     print(value)
#
# for value in g2(range(10)):
#     print(value)
#
# # yield from iterable(list, tuple, dict...)
# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         yield from my_iterable
#         # for value in my_iterable:
#         #     yield value
#
# for value in my_chain(my_list, my_dict, range(5,10)):
#     print(value)

def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None) # 直接发到gen中了

# 1.main调用方,g1委托生成器,gen子生成器
# 2.yield from会在调用方与子生成器之间建立一个双向通道
