import asyncio
import sys
import itertools

async def heavy():
    await asyncio.sleep(3)
    return 'done.'


async def spin():
    write, flush = sys.stdout.write, sys.stdout.flush
    for c in itertools.cycle('|/-\\'):
        write(f'\r{c}')
        flush()
        try:
            await asyncio.sleep(0.3)
        except asyncio.CancelledError:
            break
    print()


async def task():
    done, pending = await asyncio.wait(
        [spin(), heavy()], return_when=asyncio.FIRST_COMPLETED
    )
    for task in pending:
        task.cancel()
    return done.pop().result()


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(task())
    loop.close()
    print(f'Result: {result}')

if __name__ == '__main__':
    main()