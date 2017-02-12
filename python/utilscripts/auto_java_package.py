#!/usr/bin/env python

import os
import sys
import re

args = sys.argv
print("引数 " + str(args[1:]) + " で実行されました")


def traverse(file):
    if os.path.isfile(file):
        execute(file)
        return
    print(file)
    os.chdir(file)
    cwdl = os.listdir()
    print(cwdl)
    for i in cwdl:
        traverse(i)
    os.chdir('..')


def execute(file):
    print('done!' + file)
    if file.endswith('.java'):
        print('Java file !')
        if not check(file):
            print("edit necessary!!")
            write(file)


def check(java_file):
    pkg_pattern = r"\s*package"
    comment_pattern = r"\s*/"
    f = open(java_file, 'r')
    count = 1
    while count < 5:
        s = f.readline()
        print(s)
        if re.match(comment_pattern, s):
            continue
        if re.match(pkg_pattern, s):
            return True
            break
        count += 1


def write(java_file):
    print("write start!!")
    f = open(java_file, 'r')
    original = f.read()
    f.close
    f = open(java_file, 'w')
    s = "package "
    path = []
    count = 0
    while True:
        count += 1
        path.append(os.path.basename(os.getcwd()))
        print(path)
        print(os.getcwd())
        if os.getcwd() == root:
            break
        os.chdir('..')
    for i in range(count):
        s += path.pop()
        s += "/"
    s += java_file[:-5] + ";"
    f.write(s + "\n" + original)
    print("write end!!")



os.chdir(args[1])
root = os.getcwd()
traverse(root)

