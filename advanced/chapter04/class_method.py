class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    def tomorrow(self): # 实例方法，针对实例操作
        self.day += 1

    # 将命名空间放到类中
    # 不好之处:如果类名变了,下面返回的类名也要跟着变
    @staticmethod
    def parse_from_string(date_str): # 不需要接self
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    # 自动传类
    # 好处:类名无需关心
    # cls-类对象 self-实例对象
    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year)>0 and (int(month)>0 and int(month)<=12) and \
                (int(day)>0 and int(day)<=31):
            return True
        else:
            return False

    def __str__(self):
        return "{year}/{month}/{day}".format(\
            year=self.year, month=self.month, day=self.day)

if __name__ == "__main__":
    new_day = Date(2016,10,19)
    print(new_day)
    new_day.tomorrow() # 解释器tomorrow(new_day)
    print(new_day)

    ## 外部处理字符串格式
    date_str = "2016-12-31"
    #year, month, day = tuple(date_str.split("-"))
    #print(year, month, day)
    #new_day = Date(int(year), int(month), int(day))
    #print(new_day)

    # static method
    new_day = Date.parse_from_string(date_str)
    print(new_day)

    # class method
    new_day = Date.from_string(date_str)
    print(new_day)

    print(Date.valid_str("2016-10-19"))
    print(Date.valid_str("2016-12-32"))
