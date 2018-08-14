# 1.用锁会影响性能
# 2.容易引起死锁问题

# RLock，可重入的锁
# 在同一个线程里面，可以连续调用多次acquire
# 一定要注意acquire的次数要和release的次数相等
'''
互相等待死锁
A(a,b)
acquire(a)
acquire(b)

B(a,b)
acquire(b)
acquire(a)

'''
from threading import Lock, RLock

total = 0

lock = Lock()
rlock = RLock()
def add():
    global total
    for i in range(1000000):
        lock.acquire() # 获取锁
        #lock.acquire() # 调用多次就会造成死锁
        # foo(lock) 子函数里又用到lock.acquire，造成死锁
        # 如果同一个线程中要用到lock多次，则使用RLock，方法一样
        total += 1
        lock.release() # 释放锁，否则其他线程将不能运行

def desc():
    global total
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(total) # 正确值应该是0，但是这里是随机值


'''
def add1(a):
    a += 1
四步操作
1. load a
2. load 1
3. +
4. store a

 26           0 LOAD_FAST                0 (a)
              2 LOAD_CONST               1 (1)
              4 INPLACE_ADD
              6 STORE_FAST               0 (a)

import dis
print(dis.dis(add1))
print(dis.dis(desc1))
'''
