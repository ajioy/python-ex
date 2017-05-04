prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 200}
print("p1:", p1)
tech_names = {'APPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print("p2:", p2)
p3 = {key:prices[key] for key in prices.keys() & tech_names }
print("p3:", p3)

# 大多数情况下字典推导能做到的，通过创建一个元组序列然后把它传给 dict()
# 函数也能实现。但是，字典推导方式表意更清晰，并且实际上也会运行的更快些 (在这个例子中，实际测试几乎比 dcit() 函数方式快整整一倍)。
p1 = ((key, value) for key, value in prices.items() if value > 200)
print("tuple:")
for val in p1:
    print(val)

p1 = dict((key, value) for key, value in prices.items() if value > 200)
print("dict:", p1)

