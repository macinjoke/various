
import asyncio

Seconds = [
    ('first', 5),
    ('second', 2),
    ('third', 3)
]

async def sleeping(order, seconds, hook=None):
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    return order

async def future_callback(callback):
    futures = []

    def hook(order):
        print(order)

    for s in Seconds:
        cor = sleeping(*s, hook=hook)
        f = asyncio.ensure_future(cor)
        f.add_done_callback(callback)
        futures.append(f)

    return await asyncio.wait(futures)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    results = []
    def store_result(f):
        results.append(f.result())
    loop.run_until_complete(future_callback(store_result))
    for r in results:
        print('future callback: {}'.format(r))


