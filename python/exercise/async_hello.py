
import asyncio
import datetime
import time

async def display_date(loop):
    end_time = loop.time() + 6.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await sleeping1(3)
        await sleeping2(1)

async def sleeping1(n):
    print('sleeping1 start')
    await asyncio.sleep(n)
    # time.sleep(n)
    print('sleeping1 end')


async def sleeping2(n):
    print('sleeping2 start')
    await asyncio.sleep(n)
    # time.sleep(n)
    print('sleeping2 end')

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.close()
