import asyncio
def callback(sleep_times):
    print("sleep {} success.".format(sleep_times))

def stoploop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    # 以下两句作用相当
    loop.call_at(now+2, callback, 2) # 在loop当前时间+2秒后执行
    loop.call_later(2, callback, 2) # 不会按代码顺序走，而是按延时时间顺序
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)
    loop.call_soon(callback, 4) # 即刻执行,但不是立即下一秒执行，而是加到队列中
    # 以上其实是loop.call_later(0, callback, 4)
    #loop.call_soon(stoploop, loop) # 即刻执行,但不是立即下一秒执行，而是加到队列中
    loop.run_forever() # 去队列中找函数运行
