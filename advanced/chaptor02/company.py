class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['tom', 'bob', 'cheer'])
company1 = company[:2]

for em in company1: # __getitem__
    print(em)

print(len(company1))
print(len(company)) # __len__