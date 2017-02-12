def my_generator():
    yield 1
    yield 2
    yield 3

print([v * 2 for v in my_generator()])
print(list(my_generator()))
print(set(my_generator()))
print(tuple(my_generator()))