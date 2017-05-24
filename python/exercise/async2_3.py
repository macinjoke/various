
Seconds = [
    ('first', 5),
    ('second', 2),
    ('third', 3)
]

import asyncio

async def sleeping(order, seconds, hook=None):
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    return order

async def parallel_by_wait():
    # execute by parallel
    def notify(order):
        print(order + ' has just finidhed.')

    # async関数の返り値はコルーチンになるので注意
    cors = [sleeping(s[0], s[1], hook=notify) for s in Seconds]
    # cors = []
    # for s in Seconds:
    #     cors.append(sleeping(s[0], s[1], hook=notify))



    done, pending = await asyncio.wait(cors)
    return done, pending


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    done, pending = loop.run_until_complete(parallel_by_wait())
    for d in done:
        dr = d.result()
        print('asyncio.gather result: {}'.format(dr))

