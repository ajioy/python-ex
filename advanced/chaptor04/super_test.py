class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        #super(B, self).__init__() #python2写法
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super(D, self).__init__()
# 既然重写B的构造函数,为什么还要去调用super?
# 复用代码
# super到底执行顺序是什么样的?
# 并不是调用父类的构造方法,而是调用MRO上一级的类构造方法

if __name__ == "__main__":
    print(D.__mro__)
    d = D()
