def add(a, b):
    a += b
    return a

class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)

if __name__ == "__main__":
    a = 1
    b = 2
    c = add(a, b) # a是不可变对象
    print(a) # 3

    a = [1, 2]
    b = [3, 4]
    c = add(a, b)
    print(a) # [1,2,3,4] # a是可变对象


    a = (1, 2)
    b = (3, 4)
    c = add(a, b)
    print(a) # (1,2)a是不可变对象

    comp1 = Company("comp1", ["ajioy1", "ajioy2"])
    comp1.add("ajioy3")
    comp1.remove("ajioy1")
    print(comp1.staffs) # ['ajioy2', 'ajioy3']

    print(Company.__init__.__defaults__) # 默认值

    comp2 = Company("comp2")
    comp2.add("ajioy4")
    print(comp2.staffs) # ['ajioy4']

    comp3 = Company("comp3")
    comp3.add("ajioy5")
    print(comp3.staffs) # ['ajioy4', 'ajioy5']
    print(comp2.staffs is comp3.staffs) # True
    # 以上这个错误是因为Company类的staffs默认为空列表，comp2和comp3的staffs指向了同一个列表对象
    # comp1传了自己的列表，没有使用默认列表，不会指向默认值，所以一切正常
    # 建议不要使用空列表作为函数参数




