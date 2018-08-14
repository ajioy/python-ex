# 类也是对象，type是创建类的元类
# 动态地创建类
# 通过函数和字符串的形式实现
def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

# 通过type形式实现动态创建类
#User = type("User", (), {}) # 类名，继承基类名，属性

def say(self):
    return "I am user"
    return self.name

class BaseClass:
    def answer(self):
        return "I am baseclass"

# 实际编码时很少用type创建类,而是用MetaClass形式
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
        pass


# 元类MetaClass是控制User类实例化的过程
class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"
    pass

# python中类的实例化过程, 会道德寻找metaclass,通过metaclass去创建user类
# 如果找不到metaclass去基类中找,如果基类中找不到再去模块中找,否则才用type创建类


if __name__ == "__main__":
    #MyClass = create_class("user")
    #my_obj = MyClass()
    #print(my_obj)
    #User = type("User", (BaseClass,), {"name":"user", "say": say}) # 类名，继承基类名，属性
    #my_obj = User()
    #print(my_obj)
    #print(my_obj.name)
    #print(my_obj.say())
    #print(my_obj.answer())
    user = User("ajioy")
    print(user)