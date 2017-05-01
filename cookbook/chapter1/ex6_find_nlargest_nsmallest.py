import heapq

nums = [1, 8, 2, 23, 7, -4, 24, 12, 43, 2]
print(heapq.nlargest(3, nums)) # [43，24，23]
print(heapq.nsmallest(1, nums)) # [－4]

portfolio = [
    {'name':'IBM', 'shares':100, 'price':91.1},
    {'name':'APPL', 'shares':50, 'price':543.22},
    {'name':'FB', 'shares':200, 'price':21.03},
    {'name':'YHOO', 'shares':45, 'price':16.38},
]

# 根据字段排序
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])

print(cheap, end='\n')
print("ex:",expensive)


# 堆是重要的特性是heap[0]总是最小那个元素
# O(logN)
heap = list(nums)
heapq.heapify(heap)
print(heap)
h1 = heapq.heappop(heap) # -4
h2 = heapq.heappop(heap) # 1
h3 = heapq.heappop(heap) # 2
print(h1, h2, h3)
