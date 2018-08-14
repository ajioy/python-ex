# 生成器函数：只要函数里有yield关键字，它就不再是一个普通的函数
# 惰性求值、延迟求值
def gen_func():
    yield 1
    yield 2
    yield 3
    # 可以不停地yield


def func():
    return 1
    return 2 # 没用

# 传统递归方法实现
# 不能打印整个过程
# 斐波拉契 0 1 1 2 3 5 8 ...
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 2) + fib(index - 1)

# 改进能打印到过程
# 当index值大的时候非常消耗内存,list
def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1

if __name__ == "__main__":
    # 返回的是生成器对象, python编译字节码的时候就产生了
    gen = gen_func()
    # 迭代协议
    for value in gen:
        print(value)
    # 返回的是值
    re = func()
    print(fib(10))
    print(fib2(10))
    print(gen_fib(10))
    for item in gen_fib(10):
        print(item)
