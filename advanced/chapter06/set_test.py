# set性能很高，O(1)
# set集合　fronzenset（不可变集合）无序，不重复
s = set('abcdefee') # Iterable
#s = set(['a', 'b', 'c'])
print(s)

s = {'a', 'b'}
print(type(s))
sf = frozenset("abcdef") # 不可变，可以作为dict的key
print(sf)

# 向set添加数据
#s.add()
another_set = set("ajioy")
# 合并两个set
s.update(another_set)
print(s)
a = {'a', 'b', 'c'}
b = {'c', 'd', 'e'}
#　集合运算 | & - 并集，交集，差积
# 差积，在a中有，b中没有的元素
re_set = a.difference(b) # 'a','b'
# 相当于re_set = a - b
print(re_set)
re_set = b.difference(a) # 'd', 'e'
print(re_set)
re_set = a & b # 'c'
print(re_set)
re_set = a | b #
print(re_set)

if 'c' in re_set: # __contains__, __issubset__
    print("i am in re_set")