# def consumer():
#     r = ''
#     while True:
#         n = yield ''
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# if __name__ == '__main__':
#     c = consumer()
#     produce(c)


import asyncio


async def hello(t, m=''):
    print(f"{m}!")
    # 异步调用asyncio.sleep(1):
    while True:
        a = await asyncio.sleep(t)
        for i in range(t):
            print(f'{m}：{i + 1}')
        print(f"{m} again!")


async def world(t, m=''):
    print(m)
    a = await asyncio.sleep(t)
    for i in range(t):
        print(f'{m}：{i + 1}')
    print(f"{m} again!")
    return 2


async def to_callback(*args, **kwargs):
    print("------------------to_callback----------------------")
    print(args)
    print(kwargs)


async def main():
    task1 = asyncio.create_task(hello(5, 'hello'))
    # task1.add_done_callback(to_callback)
    task2 = asyncio.create_task(
        world(3, 'world'))
    print(await task1)
    print(await task2)


if __name__ == '__main__':
    asyncio.run(main())
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
