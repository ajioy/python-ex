# 不是很懂 5.1
# 实现一个队列，按给定的优先级来对元素排序，每次pop操作都会返回优先级最高的元素
import heapq
class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

#    def __repr__(self):
#        return 'Item({!r})'.format(self.name)
    '''
    Item('bar')
    Item('spam')
    Item('foo')
    Item('grok')
    '''

    def __str__(self):
        return 'Item({})'.format(self.name)
    '''
    Item(bar)
    Item(spam)
    Item(foo)
    Item(grok)
    '''

print(Item('spam'))
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop()) # bar
print(q.pop()) # spam
print(q.pop()) # foo
print(q.pop()) # grok
