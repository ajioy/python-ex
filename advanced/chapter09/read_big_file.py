# 500G大文件，只有1行，特殊分隔符{|}
'''
f = open()
f.read() # 一次性把文件读到内存中
f.read(4096) # 一次只读取4096个字符，内部维护偏移量
'''


def myreadlines(f, symbol):
    buf = "" # 用作缓存
    while True:
        while symbol in buf: # 缓存中是否存在分割符
            # 有分割符，则将它下标找出来
            pos = buf.index(symbol)
            yield buf[:pos] # 分割符之前的数据
            buf = buf[pos + len(symbol):] # 缓存中去掉已yield出去的部分
        chunk = f.read(4096)

        if not chunk: # 已经读到了文件结尾
            yield buf # 结尾数据
            break
        buf += chunk


with open("input.txt") as f:
    n = 0
    for line in myreadlines(f, "{|}"):
        n += 1
        print(line)
    print(n)
