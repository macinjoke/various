# coding: UTF-8

# 文字列
# 文字数 len
# 検索 find
# 切り出し [num] [start:end] [start:] [:end] [start:-end]

s = "abcdefghi"
print(s)
print(len(s))
print(s.find("c"))
print(s.find("x"))

print(s[2])
print(s[2:5])
print(s[2:])
print(s[:5])
print(s[2:-1])


print("c" in s)
