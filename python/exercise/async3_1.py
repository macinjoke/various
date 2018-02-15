# aだけ2回呼ばれる挙動謎だなー by makky

def delegator():
    while True:
        print("a")
        res = yield from subgenerator()
        print(res)  # fin
        print("hoge")

def subgenerator():
    while True:
        recv = yield
        if recv is None:
            break
        print(recv)
    return 'fin.'


g = delegator()
next(g)
g.send('A')
g.send('B')
g.send(None)
