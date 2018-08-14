# GIL:global interpreter lock 全局解释器锁
# python中一个线程对应C语言中的一个线程
# GIL使得同一个时刻只许有一个线程运行在CPU上执行字节码
# 无法将多个线程映射到多个CPU上执行，所以慢
# 线程间同步还是要考虑
# GIL会根据执行的字节码行数\时间片释放GIL, GIL遇到IO操作时主动释放

# import dis
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))

total = 0

def add():
    # 1. do something
    # 2. io操作
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(total) # 正确值应该是0，但是这里是随机值