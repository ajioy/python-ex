from datetime import date, datetime

# 如何复用检查数据是否合法的代码
# 只要实现以下三个魔法函数的其中一种即为属性描述符
# __get__, __set__, __delete__

import numbers
# 一种是
class IntField:
    # 数据描述符实现了__get__和__set__ DataDescriptor
    def __get__(self, instance, value):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

        pass

    def __delete__(self, instance, owner):
        pass

class NonDataIntField:
     # 实现了__get__  非数据属性描述符
    def __get__(self, instance, value):
        return self.value

class User:# 对应数据库表
    age = IntField()  # age是一个属性描述符对象


if __name__ == "__main__":
    usr = User()
    usr.age = 30 # 对age属性描述符赋值时会调用__set__方法
    #usr.age = "abc" # ValueError: int value need
    #usr.age = -1
    print(usr.age)
    print(getattr(usr, 'age'))
    usr.__dict__['age'] = 31
    print(usr.__dict__)

    pass

'''
如果user是某个类的实例，那么user.age（以及等价的getattr(user,'age'))
首先调用__getattribute__
如果类定义了__getattr__方法，那么在__getattribute__抛出AttributeError的时候
会调用到__getattr__，
而对于描述符(__get__)的调用，则是发生 在__getattribute__内部的。
user = User()，那么user.age顺序如下
1>如果"age"是出现在User或其基类的__dict__中，且age是data descriptor，
    那么调用数据描述符中的__get__方法
2>如果"age"出现在user对象的__dict__中,那么直接返回user.__dict__['age'],否则
3>如果"age"出现在User或其基类的__dict__中
    3.1>如果age是non-data descriptor,那么调用其__get__方法,否则
    3.2>返回__dcit__['age']
4>如果User有__getattr__方法,调用__getattr__方法,否则
5>抛出AttributeError异常
'''