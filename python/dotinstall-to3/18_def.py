# coding: UTF-8
# 関数 def
# 引数
# 返り値
def hello(name, num = 3):
    print("hello %s! " % name * num)

hello("tom", 2)
hello(num = 2, name = "tom")
hello("alice", 3)
hello("charlie")

def hello2(name, num = 5):
    return "hello %s! " % name * num

s = hello2("steve")
print(s)

