from chaptor04.class_method import Date
class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_birthday(self):
        return self.__birthday

    def get_age(self):
        return 2016 - self.__birthday.year

if __name__ == "__main__":
    user = User(Date(1990,2,1))
    #print(user.birthday)
    print(user.get_birthday())
    #print(user.__birthday) # 无法通过实例访问私有属性，只能通过公共方法
    print(user._User__birthday) # 实际上只是把名称进行了一个变形，还是可以访问，_classname__attr
    print(user.get_age())