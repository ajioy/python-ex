import os
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
import os
files = os.listdir('./')
if any(name.endswith('.py') for name in files): # 疑惑这句代码的构成
    print("there be python!")
else:
    print("sorry, no python.")

s = ('AJIOY', 50, 123.45)
print(s)
print(','.join(str(x) for x in s))
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)  # return 20
'''
# 理解成以下
lst = []
for s in portfolio:
    lst.append(s['shares'])
min(lst)
'''
print(min_shares)


# 生成器表达式作为参数传给函数时，可以省去括号
s = sum((x * x for x in nums))
print(s)
# 以上等效于
s = sum(x * x for x in nums)
print(s)

# 用临时列表的方式不如以上优雅高效,生成器是以迭代的方式转换数据，更省内存
s = sum([x * x for x in nums])
print(s)

min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares) # Alternative: Returns {'name': 'AOL', 'shares': 20}
