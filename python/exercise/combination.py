from math import factorial as f
from math import pow as p
from functools import reduce

def combination(n, r):
    return int(f(n) / (f(r) * f(n - r)))


def correlation_rule_sum(m):
    return int(sum(combination(m, k) * (p(2, k) - 2) for k in range(2, m + 1)))

col_sum = correlation_rule_sum(5)
s = col_sum * 200
ans_s = s / (1.6 * p(10, 6))
ans_m = ans_s / 60
ans_h = ans_m / 60
print(col_sum)
print(s)
print(str(ans_s) + " (sec)")
print(str(ans_m) + " (minute)")
print(str(ans_h) + " (hour)")


# # result = reduce(lambda a, x: a * combination(x, 10), range(80, 0, -10), 1)
# result = 1
# for i in range(80, 0, -10):
#     result *= combination(i, 10)
# print(result / 1)
# print(result / 10000000)
# print(result / 10000000 / (60 * 60 * 24 * 365))
# print(pow(8, 80) / 1)
# print(pow(8, 80) / 10000000)
# print(pow(8, 80) / 10000000 / (60 * 60 * 24 * 365))

