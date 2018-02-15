import asyncio
import random

async def hoge():
    count = 0
    while True:
        await asyncio.sleep(0.5)
        print("* {}".format(count))
        count += 1
        i = random.randint(1, 3)
        if i == 1:
            break
    return count

async def fuga():
    count = 0
    while True:
        print("- {}".format(count))
        count += 1
        i = random.randint(1, 3)
        if i == 1:
            break
    return count

async def manage():
    count = 0
    total = 0
    while True:
        print("[{}]".format(count))
        count += 1

        result = await hoge()
        print("{} 回実行された".format(result))
        subtotal = result
        result = await fuga()
        print("{} 回実行された".format(result))
        subtotal += result
        print("第{}ラウンドでは計 {}回実行された".format(count, subtotal))
        total += subtotal

        i = random.randint(1, 3)
        if i == 1:
            break
    print("合計で {}回実行された".format(total))


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(manage())

if __name__ == '__main__':
    main()
