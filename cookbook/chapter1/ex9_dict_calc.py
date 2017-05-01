prices = {
    'ACME':45.23,
    'AAPL':612.23,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

# zip将字典的键和值反转
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
        
print(min_price)
print(max_price)


prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# zip()创建了一个抚今追昔器，它的内容只能被消费一次
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
#print(max(prices_and_names)) # valueError: max() arg is an empty sequence

print(min(prices)) # returns 'AAPL'
print(min(prices.values())) # return 10.75

print(min(prices, key=lambda k: prices[k])) # returns 'FB'
print(max(prices, key=lambda k: prices[k])) # returns 'AAPL'

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)
