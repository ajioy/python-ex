# new可以自定义类的生成过程,添加额外的逻辑
# new控制对象的生成过程，运行在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象，则不会调用init函数
# new是框架中用得非常频繁
class User:
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)
        pass

    # 只是用于初始化实例
    def __init__(self, name):
        print("in init")
        self.name = name
        pass

if __name__ == "__main__":
    user = User("ajioy")
