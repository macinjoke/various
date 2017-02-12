# coding: UTF-8

# 条件分岐 if
# 比較演算子 > < >= <= == !=
# 論理演算子 and or not

score = 70
if score > 60:
    print("ok!")
elif score > 40:
    print("soso...")
else:
    print("ng!")

print("OK!" if score > 60 else "NG!")
