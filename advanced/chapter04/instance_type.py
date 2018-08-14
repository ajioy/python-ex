class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) == B) # ==判断值是否相同
print(type(b) is B) # is判断id是否相同
print(type(b) is A) # False,id不相等
