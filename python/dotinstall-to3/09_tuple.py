# coding: UTF-8

# タプル(変更できない)

a = (2, 5, 8)
# len + * []
print(len(a)) # 3
print(a * 3)
print(a[1:])

# a[2] = 10 # エラーになる

# タプル <> リスト
b = list(a)
print(b)
c = tuple(b)
print(c)
