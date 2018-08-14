# python和c++/java的变量在本质上是不同的
# c++定义一个变量后就会在内存中开辟一个相应大小的空间(盒子)
# python只是把变量贴在对象上,指针指向对象,理解为便利贴,大小固定,可以贴在任何对象上
a = 1 # 在内存中开辟一块空间存取1,a指向1上
a = "abc"

a = [1,2,3]
b = a
b.append(4)
print(a)
print(a is b) # True,同一个对象
print(id(a), id(b)) # id一致

a = [1,2,3,4]
b = [1,2,3,4]
print(a is b) # False,它们只是值相同,是不同的对象
print(id(a), id(b)) # id不相同
a = 1
b = 1
print(a is b) # True,小整数在内存中是唯一的
print(id(a), id(b)) # id相同
a = "abc"
b = "abc"
print(a is b) # True,小字符串在内存中也是唯一的
print(id(a), id(b)) # id相同

print(a == b) # True 调用魔法函数__eq__,判断值是否相等

class Person:
    pass

person = Person()
if type(person) == Person:
    print("YES")

# 推荐用以下方法
if isinstance(person, Person):
    print("YES")
