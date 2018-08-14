#列表生成式（列表推导式）
# 1.提取1-20之间的奇数
odd_list = []
for i in range(20):
    if i % 2 == 1:
        odd_list.append(i)

print(odd_list)

# 列表生成式
odd_list = [x for x in range(20) if x % 2 == 1]
print(odd_list)
print(type(odd_list)) # class 'list'

# 2.逻辑复杂情况的列表生成式
def handle_item(item):
    return item * item

odd_list = [handle_item(x) for x in range(20) if x % 2 == 1]
print(odd_list)

# 生成器表达式
odd_gen = (x for x in range(20) if x % 2 == 1)
print(type(odd_gen)) # <class 'generator'>
for x in odd_gen:
    print(x)

# 生成器转成列表
new_list = list(odd_gen)
print(type(new_list))
print(new_list) # ? 打印出来是空的,奇怪

# 字典推导式
my_dict = {"ajioy1": 23, "ajioy2": 15, "tom": 28}
reversed_dict = {value: key for key, value in my_dict.items()}
print(type(reversed_dict)) # <class 'dict'>
print(reversed_dict)

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)
my_set = set(my_dict.keys())
print(type(my_set))
print(my_set)

