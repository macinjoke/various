def divide(x, y):
    try:
        print("devide {0} by {1}".format(x, y))
        result = x / y
    except ZeroDivisionError:
        print("division by zero!!")
    else:
        print("result is ", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")
