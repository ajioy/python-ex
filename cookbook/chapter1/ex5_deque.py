from collections import deque
# 当有新记录加入队列时已满时会自动移除最老的那条记录
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q) # [1,2,3]
q.append(4)
print(q) # [2,3,4]

# 无限队列
# 从队列两端添加或弹出元素的复杂度都是O(1)
# 相比列表，当从列表头部插入或移除元素时，列表复杂度为O(N)
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q) # [1,2,3]
q.appendleft(4) 
print(q) # [4,1,2,3]
q.pop()
print(q) # [4,1,2]
q.popleft()
print(q) # [1,2]
