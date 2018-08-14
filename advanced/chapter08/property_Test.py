from datetime import date, datetime
class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    # 计算属性
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


#usr = User("ajioy", date(year=1990, month=12, day=31))
if __name__ == "__main__": # 不这样写的话，其他模块导入本模块时，会执行上面注释的代码
    usr = User("ajioy", date(year=1990, month=12, day=31))
    #print(usr.get_age())
    print(usr.age) # 28
    usr.age = 30
    print(usr.age) # 28
    print(usr._age) # 30
