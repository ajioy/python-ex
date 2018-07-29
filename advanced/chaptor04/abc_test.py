# 我们去检查某个类是否有某个方法

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(["ajioy1", "ajioy2"])
if hasattr(company, "__len__"):
    print(len(company))

# 在某些情况下希望判定某个对象的类型
from collections.abc import Sized
print(isinstance(company, Sized))

# 需要强制某个子类必须实现某些方法
# Web框架，集成cache(redis, cache, memorycache)
# 需要设计一个抽象基类，指定子类必须实现某些方法


# 考虑扩展性的时候
import abc

#class CacheBase:
#    def get(self, key):
#        raise NotImplementedError
#
#    def set(self, key, value):
#        raise NotImplementedError
#
#
import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        raise NotImplementedError

class RedisCache(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        print(key, value)

redis_cache = RedisCache() # 希望在实例化的时候抛异常，引用abc模块
#redis_cache.set("key", "value") # 没有定义此方法时会抛异常

