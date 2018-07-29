class A:
    name = "A"
    def __init__(self):
        self.name = "obj"

a = A()
print(a.name) # 由下而上，先查实例变量，再查类变量

#class D:
#    pass
#
#class C(D):
#    pass
#
#class B(D):
#    pass
#
#class A(B,C):
#    pass
#
#print(A.__mro__)

class D:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B,C):
    pass

print(A.__mro__)
