aList = [3,4,5,6,7,9,11,13,15,17]
print(aList[::]) # 返回包含原中所有元素的新列表
print(aList[::-1]) # 返回包含原列表中所有元素的逆序列表
print(aList[::2]) # 隔一个取一个，获取偶数位置的元素
print(aList[1::2]) # 隔一个取一个，获取奇数位置的元素
print(aList[3:6]) # 指定切片的开始和结束位置，[3,6)，不包含6
print(aList[0:100]) # 切片结束位置大于列表长度时，从列表尾部截断
print(aList[100:]) # 切片开始位置大于列表长度时，返回空列表

aList[len(aList):] = [9] # 在列表尾部增加元素
print(aList)
aList[:0] = [1,2] # 在列表头部插入元素,相当于aList = [1,2] + aList
print(aList)
aList[3:3] = [4] # 在中间位置插入元素
print(aList)
aList[:3] = [10,11] # 替换列表元素,将[0,3)的内容替换成[10,11],等号两边的列表长度相等
print(aList)
aList[3:] = [4,5,6] # 替换,将[3,最后]的元素替换成[4,5,6]等号两边的列表也可以不相等
print(aList)
aList[::2] = [0] * 3 # 隔一个修改一个，都修改为0
print(aList)
aList[::2] = ['a', 'b', 'c'] # 隔一个修改一个
print(aList)
#aList[::2] = [1,2] # 左侧切片不连续，等号两边列表长度必须相等
aList[:3] = [] # [0，3）置空，即清空前三个元素
print(aList)

aList = [1,2,3,4,5,6]
del aList[:3] # 切片元素连续
print(aList)
del aList[::2] # 切片元素不连续，隔一个删除一个
print(aList)



