class MyIterator:
    def __init__(self, *numbers):
        self._numbers = numbers
        self._i = 0

    def __iter__(self):
        # next()はselfが実装しているのでそのままselfを返す
        return self

    def __next__(self):
        if self._i == len(self._numbers):
            raise StopIteration()
        value = self._numbers[self._i]
        self._i += 1
        return value

my_iterator = MyIterator(10, 20, 30)
for num in my_iterator:
    print('hello %d' % num)



