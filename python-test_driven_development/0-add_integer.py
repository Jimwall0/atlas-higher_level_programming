#!/usr/bin/python3
def add_integer(a, b=89):
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    elif not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a or b must be an integer or float")
    return a + b
