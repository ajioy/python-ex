# coding:utf-8
# decorator ex2

#带参数的装饰器
def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):
            before_result = before_func(request, kargs)
            if (before_result != None):
                return before_result

            main_result = main_func(request, kargs)
            if(main_result != None):
                return main_result

            after_result = after_func(request, kargs)
            if(after_result !=  None):
                return after_result
        return wrapper
    return outer

def BeforeFoo(request, kargs):
    print("before foo():%s "% request)

def AfterFoo(request, kargs):
    print("after foo(): %s %s" % (request, kargs))
    
@Filter(BeforeFoo, AfterFoo)
def Foo(request, kargs):
    print("Foo is running: %s %s" % (request, kargs))

Foo('hello', 'ajioy')

'''
#类装饰器
class Foo(object):
    def __init__(self, func):
        self._func = func
        
    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()
'''


'''
#带参数的装饰器
class  logging:
    def info(str):
        print(str)
    def warn(str):
        print(str)

        
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level = "warn")
def foo(name='foo'):
    print("i am %s " % name)

foo()
'''

'''
#before decorator
def use_logging(func):
    logging.warn("the function (%s) is running" % func.__name__)
    func()
    
def foo():
    print('i\'m foo')
    logging.info("foo is running")

#foo()
#use_logging(foo) 改变了原始函数调用方式、逻辑结构
'''

'''
#simple decorator
def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn("function (%s) is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@use_logging
def bar():
    print('i am bar')

@use_logging
def foo():
    print('i am foo')

bar()
foo()

'''
'''
横切面(Aspect)
bar = use_logging(bar)
bar()
'''






