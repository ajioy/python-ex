# def get_url(url):
#     # do something
#     html = get_html(url) # 耗时,阻塞等待,切换到另一个函数执行
#     # parse html
#     urls = parse_url(html) #CPU完成

# 传统函数调用过程A->B->C
# 需要一个可以暂停的函数,并且可以在适当的时候恢复该函数继续执行
# 协程-有多个入口的函数,可以暂停的函数,可以向暂停的地方传入值

def gen_func():
    # 可以将url值产生给外部使用
    # 可以接收调用方传来的值
    html = yield "http://blog.csdn.net/ajioy" # 值会传递回来
    print("recv:",html)
    yield 2
    yield 3
    return "ajioy"

# 1.生成器既可以产生值,也可以接收值
# 2.启动生成器有两种方式:next(), send()
# 3.在调用send发送非None值之前,必须启动一次生成器,方式有两种,next()或gen.send(None)
if __name__ == "__main__":
    gen = gen_func()
    url = next(gen) # gen.send(None)
    print("url:", url)
    recv = gen.send("hello") # send可以将传值进生成器内部,同时还可以重启生成器执行到下一个yield的位置
    print(recv)

    print(next(gen))
    #print(next(gen))
    #print(next(gen))
