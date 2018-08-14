# __getattr__在查找不到属性的时候调用
# __getattribute__ 任何情况下返回该函数

from datetime import date
class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info
        self._age = 0

    def __getattr__(self, item):
        return self.info[item]
        # print("not found attr")

    # 无条件执行此魔法函数，屏蔽了其他所有属性
    # 把持了所有函数的入口，更多用于框架的编写中，平时不建议使用
    def __getattribute__(self, item):
        return "ajioy"

if __name__ == "__main__":
    usr = User("ajioy", date(year=1990, month=12, day=31), info={"company": "Google"})
    #usr.age # 不存在这个属性，则会走到__getattr__
    print(usr.company)
