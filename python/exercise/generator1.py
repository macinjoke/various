def my_generator():
    print('before yield')
    yield 1
    print('yielded 1')
    yield 2
    print('yielded 2')
    yield 3
    print('yielded 3, finished')


gen = my_generator()
print('start')
v1 = gen.__next__()
print('called __next__(), v1 = %s' % v1)
v2 = gen.__next__()
print('called __next__(), v2 = %s' % v2)
v3 = gen.__next__()
print('called __next__(), v3 = %s' % v3)
from time import sleep
sleep(0.1)
v4 = gen.next() # should be exception

