# 不建议继承list和dict
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

# Ｃ语言写的dict某些情况下不会调用子类的覆盖方法
my_dict = Mydict(one=1) # 实际上并没有调用魔法函数Mydict.__setitem__
my_dict["one"] = 1 # 魔法函数生效
print(my_dict)

from collections import UserDict
# 用python重写过逻辑


class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
print(my_dict)

from collections import defaultdict


# __missing__方法
my_dict = defaultdict(dict)
my_value = my_dict["ajioy"]
pass