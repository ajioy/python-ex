# coding:utf-8
#decorator ex
#add a new func don't change func anything

def outer(func):
    def inner(arg1, arg2):
        print("do something before func()")
        #return func(arg1, arg2) don't do that ,the next code will not be excuted.
        res = func(arg1, arg2)
        print("ok,after func()")
        return res
    return inner

@outer
def func(arg1, arg2):
    print("Run func() %s %s" % (arg1, arg2) )
    return 'i\'m ok!'


print(func('ajioy', 'is a boy'))


'''
============== RESTART: E:/Git/python-ex/basic ex/decorator.py ==============
do something before func()
Run func() ajioy is a boy
i'm ok!
>>> 
============== RESTART: E:/Git/python-ex/basic ex/decorator.py ==============
do something before func()
Run func() ajioy is a boy
ok,after func()
i'm ok!
>>> 
'''
