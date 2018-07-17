import string
import random
print(string.ascii_lowercase)
print(random.choice(string.ascii_lowercase))
print([random.choice(string.ascii_lowercase) for i in range(20)])
print(''.join([random.choice(string.ascii_lowercase) for i in range(20)]))
random_strs = [
    ''.join([
        random.choice(string.ascii_lowercase) for i in range(20)
    ]) for i in range(10000)
]
print(random_strs)
print(random.choice(['alice', 'bob']))
print(random.choice([True, False]))
print(random.randint(10, 90))
li = [i for i in range(10000)]
print(li)
print(type(li[10]))
