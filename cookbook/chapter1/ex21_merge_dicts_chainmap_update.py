a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a, b)
print(c['x']) # 1 from a
print(c['y']) # 2 from b
print(c['z']) # 3 from a 

print(len(c)) # 3
print(list(c.keys())) # ['x', 'y', 'z'],不稳定，顺序会随机
print(list(c.values())) # 同上

# 如果存在重复键，第一次出现的映射值会被返回，总是a中对应的值

# 对于字典的更新或删除操作总是影响的是列表中第一个字典a
c['z'] = 10
c['w'] = 40
print(c)
del c['x']
print(c)
#del c['y'] # 会报错

values = ChainMap()
values['x'] = 1
print(values)
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values) # ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x']) # 3,last element

values = values.parents
print(values) # ChainMap({'x': 2}, {'x': 1})
print(values['x']) # 2
values = values.parents
print(values['x']) # 1

# 用update合并字典, 效果跟ChainMap一致
print(50 * "-")
a = {'a': 1, 'c': 3}
b = {'b': 2, 'c': 4}
merged = dict(b)
merged.update(a) 
print(merged)
print(merged['a'])
print(merged['b'])
print(merged['c'])

a = {'x': 1, 'z': 2}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged)
print(merged['x'])
a['x'] = 42
print(merged['x'])
