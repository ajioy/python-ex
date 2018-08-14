from collections.abc import Mapping, MutableMapping
# dict属于mapping类型

a = {}
# a并非继承自MutableMapping，只是实现了它其中的一些方法，一些魔法函数
#MutableMapping.register(dict)
print(isinstance(a, MutableMapping))
