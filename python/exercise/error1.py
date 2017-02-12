import sys
import time

print("hello, error test")

try:
    f = open('test.txt')
    while True:
        line = f.readline()
        s = line.strip()
        if s == "":
            continue
        i = int(s)
        time.sleep(1)
        print(i)
except OSError as e:
    print("OS error: {0}".format(e.filename))
except ValueError:
    print("intに変換できんかったぞ")
except:
    print("Unexpected errorだべ: ", sys.exc_info()[0])
    raise
else:
    print("エラーが出なかったらここが実行されるぞ")
print("終わり")

