# 删除序列相同元素并保持顺序
def dedupe(items): # hashable
    seen = set()
    for item in items:
        if item not in seen:
            yield item   # keep the order
        seen.add(item)   # no order 无序

    print("no order",seen)

aa = [1, 5, 2, 1, 9, 1, 5, 10]
lst = list(dedupe(aa))
print(lst)


def dedupe(items, key=None): # dict
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# 不太懂5.2
lst = list(dedupe(a, key=lambda d: (d['x'], d['y']))) # 去重x,y
print(lst)
lst = list(dedupe(a, key=lambda d: (d['x']))) # 去重x
print(lst)

# 仅仅是去重，不讲顺序则可用set
b = set(aa)
print(b)
