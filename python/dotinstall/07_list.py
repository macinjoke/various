# coding: UTF-8

# リスト (文字列に使った命令をいくつか使えるぜ)
test = [100, 200, "string"] # 型が違くてもok

sales = [255, 100, 353, 400]
print len(sales) #4
print sales[2] #353
sales[2] = 100
print sales[2]
sales[2] = 353
print sales[1:]

# in
print 100 in sales #True

# range range(num) range(start, end) range(start, end, interval)
print range(10)
print range(3, 10)
print range(3, 10, 2)
