# python中函数的工作原理
'''

python.exe会用一个叫PyEval_EvalFrameEx(C函数)去执行foo函数,
首先会创建一个栈帧(stack frame)
栈帧对象(上下文),代码变为字节码对象
调用foo前,会创建一个栈帧对象
当foo调用子函数bar时,又会创建一个栈帧对象,将函数的控制权交付给bar
所有的栈帧都是分配在堆内存上,这就决定了栈帧可以独立于调用者存在

# 生成器对象通过栈帧的特性,实现暂停和继续前进
# 生成器对象也是分配在堆内存中，只要拿到栈帧对象，可以在任何对象里、函数里、模块里控制暂停或恢复
# 协程===
'''
import dis
import inspect
frame = None

def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()
    pass

def gen_func():
    yield 1
    name = "ajioy"
    yield 2
    age = 30
    return "ajioy is a goodboy"


if __name__ == "__main__":
    print(dis.dis(foo)) # 字节码对象
    '''
     11           0 LOAD_GLOBAL              0 (bar)
                  2 CALL_FUNCTION            0
                  4 POP_TOP
                  6 LOAD_CONST               0 (None)
                  8 RETURN_VALUE
    '''
    foo()
    print(frame.f_code.co_name)
    caller_frame = frame.f_back
    print(caller_frame.f_code.co_name)

    gen = gen_func()
    print(dis.dis(gen))
    '''
     24           0 LOAD_CONST               1 (1)
                  2 YIELD_VALUE
                  4 POP_TOP
    
     25           6 LOAD_CONST               2 ('ajioy')
                  8 STORE_FAST               0 (name)
    
     26          10 LOAD_CONST               3 (2)
                 12 YIELD_VALUE
                 14 POP_TOP
    
     27          16 LOAD_CONST               4 (30)
                 18 STORE_FAST               1 (age)

     28          20 LOAD_CONST               5 ('ajioy is a goodboy')
                 22 RETURN_VALUE
    '''
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    '''
    -1 # 表示还没有开始执行
    {}
    '''
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    '''
    2 # 跳到字节码2 YIELD_VALUE
    {}
    '''
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    '''
    12 # 跳到字节码12 YIELD_VALUE
    {'name': 'ajioy'} # 局部变量
    '''
    # 实现暂停和继续前进

