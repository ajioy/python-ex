from collections import namedtuple
# 命名元组的一个主要用途是将你的代码从下标操作中解脱出来
Subscriber = namedtuple('Subscriber', ['addr','joined'])
print(Subscriber)
sub = Subscriber('ajioy@hotmail.com', '2014-5-4')
print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr, joined = sub
print(addr, joined)

'''
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total
'''

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shareds * s.price
    return total

s = Stock('AJIOY', 100, 123.45)
print("stock:", s)
name, shares, price = s
print(name, shares, price)
# s.price = 75 # wrong, you can't change
# 用_replace()方法，它会创建一个全新的命名元组并将对应的字段用新值取代
s = s._replace(shares = 75)
print(s)Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
_, shares, _ = s
print(shares)

# _replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候， 它是一个非常方便的填充数据的方法
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s) # **s 是啥意思

a = {'name': 'AJIOY', 'shares': 100, 'price': 123.45 }
ss = dict_to_stock(a)
print(ss)

b = {'name': 'AJIOY', 'shares': 100, 'price': 123.45, 'date': '5/4/2014'}
ss = dict_to_stock(b)
print(ss)


