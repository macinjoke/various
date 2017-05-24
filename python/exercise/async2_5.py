
import asyncio

async def sleeping(order, seconds, hook=None):
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    return order

async def limited_parallel(limit=5):
    sem = asyncio.Semaphore(limit)

    def hook(order):
        print(order)

    # function want to limit the number of parallel
    async def limited_sleep(num):
        with await sem:
            return await sleeping(str(num), num, hook=hook)
        # return await sleeping(str(num), num, hook=hook)

    import random
    tasks = [limited_sleep(random.randint(0, 3)) for _ in range(9)]
    return await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    done, pending = loop.run_until_complete(limited_parallel())
    for d in done:
        print("limited parallel: {}".format(d.result()))
