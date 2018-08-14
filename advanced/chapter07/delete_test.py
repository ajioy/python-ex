# python中垃圾回收的算法是采用引用计数
# 当引用计数器减到0的时候，解释器会回收这个对象
#a = 1
#b = a # 1这个对象的引用计数为2
#del a # 此时对1这个对象的引用计数减1，并且清理掉了变量a
#print(b) # 1
##print(a) # NameError: name 'a' is not defined

a = object()
b = a
del a
print(b) # 正常
# print(a) # NameError

class A:
    def __del__(self): # 当解释器回收资源的时候会调用这个魔法函数
        pass


