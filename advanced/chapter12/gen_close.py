# GeneratorExit是继承自BaseException
def gen_func():
    # try:
    #     html = yield "http://blog.csdn.net/ajioy" # 值会传递回来
    # # except GeneratorExit:
    # #     pass
    # # 如果close之后还有yield,调用close会抛出异常
    # # except GeneratorExit:
    # #     raise StopIteration # 不会抛
    # # except Exception:  # 不会抛
    # #     pass
    # except BaseException:
    #     pass
    try:
        yield "www.baidu.com"
    except Exception:
        pass
    yield 2
    yield 3
    return "ajioy"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
    print(next(gen))
    gen.throw(Exception, "download error")
    #gen.close()
    #next(gen)