class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2,3)
print(a.x, a.y, a.aa)

a.aa = 100
print(A.aa)
print(a.aa) # a对象内部新建了一个类变量aa，非类变量aa
A.aa = 111
print(A.aa)
#print(A.x) # x是实例变量，类名不能直接访问
