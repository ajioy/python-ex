# 命名切片
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
# 鬼知道你record[20:23]是表示什么,硬编码下标无法理解
SHARES = slice(20,23)
PRICE = slice(31,37)
# 用切片对象，如此一来，一目了然
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(a)
print(items[2:4])
print(items[a])
items[a] = [10,11] # replace 2,3
print(items)
del(items[a])
print(items)

a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = "hello,ajioy"
print("len:",len(s))
print("a:",a)
sss = a.indices(len(s)) # (start, stop, step)
print("sss:",sss)
print("*a:", *a.indices(len(s))) # [5, 11, 2]
for i in range(*a.indices(len(s))):
    print(s[i])

