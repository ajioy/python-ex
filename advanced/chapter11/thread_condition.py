import threading

# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}: 在 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{}: 好啊 ".format(self.name))
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猎精灵")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}: 小爱同学".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{}: 我们来对古诗吧".format(self.name))
#         self.lock.release()

# 通过condition完成协同

from threading import Condition
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait() # 第一句话是天猫精灵说的，所以要等
            print("{}: 在 ".format(self.name))
            self.cond.notify()

            self.cond.wait() # 第一句话是天猫精灵说的，所以要等
            print("{}: 好啊 ".format(self.name))
            self.cond.notify()

class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猎精灵")
        self.cond = cond

    def run(self):
        # 可以将with更换成self.cond.acquire和release组队的形式
        # 效果是一样的,但with的用法更直观
        with self.cond:
            print("{}: 小爱同学".format(self.name))
            self.cond.notify() # 通知
            self.cond.wait() # 等待小爱的通知

            print("{}: 我们来对古诗吧".format(self.name))
            self.cond.notify() # 通知
            self.cond.wait() # 等待小爱的通知

if __name__ == "__main__":
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 启动顺序很重要
    # 在调用with cond之后才能调用wait或notify方法
    # condition有两层锁，一把是底层会在线程调用了wait方法的时候释放
    # 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
    #tianmao.start() # tianmao先执行就会陷入僵局
    xiaoai.start()
    tianmao.start()

    # 如果需要进一步了解condition，建议看源码
