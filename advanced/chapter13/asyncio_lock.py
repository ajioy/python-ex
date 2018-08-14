import asyncio

total = 0


async def add():
    global total
    # 凡是那些不是await开头的代码,都会等它执行完毕才会走下一步
    for i in range(100000):
        total += 1

async def desc():
    global total
    for i in range(100000):
        total -= 1

if __name__ == "__main__":
    tasks = [add(), desc()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)