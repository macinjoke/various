print('reduce fizzbuzz')
from functools import reduce
print(reduce(lambda a, x: "{}\n{}".format(a, 'FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x), range(1, 101)), '')

print()
print()
print('join fizzbuzz')
print('\n'.join(['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else str(x) for x in range(1, 101)]))

print()
print()
print('join fizzbuzz 2')
print('\n'.join([(('' if x % 3 else 'Fizz')+('' if x % 5 else 'Buzz')) or str(x) for x in range(1, 101)]))
