# format()和format_map()与其他方式相比更加先进
# 只是对缺少变量支持不好
s = '{name} has {n} messages.'
print(s.format(name='Ajioy', n=12))

name = 'Ajioy'
n = 12
# 替换的变量能在变量域中找到，用fomat_map()与vars()结合
print(s.format_map(vars()))

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

# 也适应于对象实例
a = Info('Ajioy', 12)
print(s.format_map(vars(a)))

class safesub(dict): # 不懂
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))

# 如果频繁操作，可将变量替换成一个工具函数封装起来
# 变量缺失也没关系
import sys

def sub(text):
# sys._getframe(1)返回调用者的栈帧，访问属性f_locals获得局部变量
    return text.format_map(safesub(sys._getframe(1).f_locals))

n = 23
print(sub('Hello, {name}'))
print(sub('you have {n} messages.'))
print(sub('your favorite color is {color}.'))

print(vars())

import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))

# 以下有问题
print('%(name) has %(n) messages.' % vars())
