# coding: UTF-8
# for ループ
sales = [13, 3523, 31, 238]
sum = 0
for sale in sales:
    sum += sale
# print sum
else:
    print(sum)

# continue & break
for i in range(10):
    if i == 3:
        # continue
        break
    print(i)
else: #break で抜けた場合はelseは実行されない
    print("done!")

