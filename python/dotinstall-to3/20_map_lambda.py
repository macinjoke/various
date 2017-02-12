# coding: UTF-8
# リスト <> 関数 map
# 無名関数

def double(x):
    return x * x

print(list(map(double, [2, 5, 8])))

print([x * x for x in [2, 5, 8]])
