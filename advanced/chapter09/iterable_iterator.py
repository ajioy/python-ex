from collections.abc import Iterator
class Company:
    def __init__(self, employee_list):
        self.employee =  employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]

class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index =0
    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

if __name__ == "__main__":
    company = Company(["ajioy", "bob", "cheer"])
    my_itor = iter(company)
    while True:
        try:
            print(next(my_itor))
        except StopIteration:
            pass

    # 以上操作相当于for循环
    #for item in company:
    #    print(item)


# 为什么for循环可以完成
# 调用for循环时,解释器会尝试调用iter(company)
# iter()函数十分智能
# 它先查找company的类中是否存在__iter__，
# 如果不存在，它会创建一个默认的迭代器，迭代器会调用__getitem__
# 如果存在，它就调用__iter__

# next()函数接收迭代器类型，不停地产生下一个对象，直到抛出异常

# 迭代器设计模式
# 不要在可迭代类型内部维护迭代器，单独抽出来