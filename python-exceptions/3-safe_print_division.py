#!/usr/bin/python3
def safe_print_division(a, b):
    total = 0
    try:
        total = a / b
        print("Inside result: {}".format(total))

    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        print("{d}".format(ZeroDivisionError))
    finally:
        return total
