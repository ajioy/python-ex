my_list = []
my_list.append(1)
my_list.append("abc")


from collections import abc

a = [1,2]
c = a + [3,4]
print(c) # [1, 2, 3, 4]

a += [5,6]
print(a) # [1, 2, 5, 6]
a += (5,6) # 可以为任意序列类型, __iadd__
print(a) # [1, 2, 5, 6, 5, 6]

c.extend(["a", "b"])
print(c)    # [1, 2, 3, 4, 'a', 'b']
c.extend(range(3))
print(c)    # [1, 2, 3, 4, 'a', 'b', 0, 1, 2]

a.append([7,9])
print(a)    # [1, 2, 5, 6, 5, 6, [7, 9]]