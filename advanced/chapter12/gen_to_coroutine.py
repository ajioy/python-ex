# 生成器是可以暂停的函数
# 用同步的方式编写异步的代码
# 在适当的时候暂停函数并在适当的时候启动函数
# 协程是单线程模式
import inspect

# 以下可以理解为协程
def gen_func():
    # 返回值给调用方，调用方通过send方式传值给gen
    value = yield 1
    return "ajioy"


if __name__ == "__main__":
    gen = gen_func()
    print(inspect.getgeneratorstate(gen)) # GEN_CREATED
    print(next(gen))
    print(inspect.getgeneratorstate(gen)) # GEN_SUSPENDED
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen)) # GEN_CLOSED

# 获取协程的返回值
