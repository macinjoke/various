# coding: UTF-8

# セット(集合型) - 重複を許さない

# a = set([1, 2, 3, 4, 3, 2]) # 重複を許さないので後の3と2は意味が無い
a = set([1, 2, 3, 4])
b = set([3, 4, 5])

#-----;これでも書ける
a = {1, 2, 3, 4}
b = {3, 4, 5}
#----


print(a)
print(b)

# - 差集合
print(a - b)
print(b - a)
# | 和集合
print(a | b)
# & 席集合
print(a & b)
# ^ どちらかにしか無い要素 (排他的論理和)
print(a ^ b)

c = set([3, 4, 6, 7])
print(a & b == a & c) # Trueを返す


