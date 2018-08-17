
from threading import Condition, Lock

if __name__ == '__main__':
    con = Condition(Lock())
    print('start')
    with con:
        print("with start")
        con.wait()
        print("with end")
