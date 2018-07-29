from chaptor04.class_method import Date
class Person:
    name = 'person'

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == '__main__':
    user = Student("HBUT")
    # 通过__dict__查询属性
    print(user.__dict__)
    # 直接通过__dict__新增属性也是可以的, 动态操控属性
    user.__dict__["school_addr"] = "ShenZhen City"
    print(user.school_addr)

    print(Person.__dict__)
    print(user.name)

    # dir 比__dict__功能更多，取的信息更加丰富，只不过没有值
    print(dir(user))

    a = [1,2]
    #print(a.__dict__) # error
    print(dir(a))
