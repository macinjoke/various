import asyncio
import sys
import itertools


@asyncio.coroutine
def heavy():
    yield from asyncio.sleep(3)
    return 'done.'


@asyncio.coroutine
def spin():
    write, flush = sys.stdout.write, sys.stdout.flush
    for c in itertools.cycle('|/-\\'):
        write(f'\r{c}')
        flush()
        # print(f'\r{c}', end="", flush=True)
        try:
            yield from asyncio.sleep(0.3)
        except asyncio.CancelledError:
            break
    print()


@asyncio.coroutine
def task():
    spinner = asyncio.async(spin())
    result = yield from heavy()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(task())
    loop.close()
    print(f'Result: {result}')

if __name__ == '__main__':
    main()