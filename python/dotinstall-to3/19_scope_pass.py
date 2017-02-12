# coding: UTF-8
# 変数のスコープ

name = "taguchi"
def hello():
    name = "fkoji"
print(name) #結果 taguchi

def hello2():
    pass

print(hello2())
hello2()
hello2()
hello2()
hello2()
hello2()
hello2()

