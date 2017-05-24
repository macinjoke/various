
import asyncio
import datetime

Seconds = [
    [
        ('first', 1),
        ('second', 2),
        ('third', 3)
    ],
    [
        ('first', 5),
        ('second', 2),
        ('third', 1)
    ]

]

start_time = datetime.datetime.now().second

async def sleeping(order, seconds, hook=None):
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    return order

async def basic_async(num):
    for s in Seconds[num]:
        r = await sleeping(*s)
        print('{}\'s {} is finished.'.format(num, r))
        print(datetime.datetime.now().second - start_time)
    return True

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(basic_async())
    asyncio.ensure_future(basic_async(0))
    asyncio.ensure_future(basic_async(1))
    loop.run_forever()


