def exe_try():
    try:
        print("code started")
        raise KeyError
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else:
        print("other error")    # 没有异常时走到这里
        return 3
    finally:
        print("finally")
        return 4
# 上下文管理器
class Sample():
    def __enter__(self): #由解释器调用
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb): # 由解释器调用
        print("exit")

    def do_something(self):
        print("do something")

if __name__ == "__main__":
    result = exe_try()
    print(result)
    with Sample() as sam:
        sam.do_something()
