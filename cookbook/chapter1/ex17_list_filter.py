mylist = [1, 4, -5, 10, -7, 2, 3, -1]
filter_list = [n for n in mylist if n > 0]
print(filter_list)
filter_list = [n for n in mylist if n < 0]
print(filter_list)

# --以上方式如果数据量大时不适用，转用以下迭代的方式
print(50 * "-")
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

print(50 * "-")
def is_odd(n):
    return n % 2 == 1

res = list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10,15]))
print(res)

print(50 * "-")
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

# 过滤的时候转换数据
print(50 * "-")
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
res = [math.sqrt(n) for n in mylist if n > 0]
print(res)


print(50 * "-")
# 将那些对应counts值大于5的地址全部输出
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n for n in counts if n > 5]
print(more5)
# 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。 然后 compress() 函数根据这个序列去选择输出对应位置为 True 的元素。
more5 = [n > 5 for n in counts]
print(more5)
res = list(compress(addresses, more5))
print(res)
