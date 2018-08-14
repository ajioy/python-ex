import numbers
class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reverse__(self):
        pass

    # 注释后会报错：TypeError: 'Group' object is not subscriptable
    def __getitem__(self, item):
        # 关键
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name,\
                       staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, \
                       staffs=[self.staffs[item]])
        #return self.staffs[item]


    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False
        pass

try:
    staffs = ["ajioy1", "neteasy123", "ajioy2", "neteasy123"]
    group = Group(company_name="neteasy123",group_name="user", staffs=staffs)
    sub_group = group[:2]
    sub_group2 = group[0]
    if "ajioy1" in group:
        print("yes")

    print("*" * 30)
    for user in group:
        print(user)
    print("*" * 30)
    pass
except BaseException as e:
    print(e)
else:
    print("normal")
finally:
    print("finished...")
