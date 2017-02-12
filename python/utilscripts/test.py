#!/usr/bin/env python

import os
import sys
from datetime import datetime

args = sys.argv
print("引数 " + str(args) + " で実行されました")

# cwd = os.getcwd()
# print(cwd)
# print(os.listdir())
# os.chdir('../..')
# cwd = os.getcwd()
# print(cwd)
# print(os.listdir())

os.chdir('/home/shunji/work/python/utilscripts')

# f = open("auto_java_package.py", "r")
# s = f.read()
# print(s)

# f = open("test_text", "a")
# f.write("スクリプトからの書き込み : " + str(datetime.now()) + "\n")

f = open("test_text", "r")
s = f.read()
print(s)

f = open("test_text")  # デフォルトのmodeは"r"

# for i in range(3):
#     s = f.readline()
#     print(s)

# s = f.readline()
# while "スクリプト" in s:
#     print(s)
#     s = f.readline()

while True:
    s = f.readline()
    print(s)
    if not s.startswith("スクリプト"): break

