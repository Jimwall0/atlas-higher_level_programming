#!/usr/bin/python3
"""
This is a test for test driven development
"""


def add_integer(a, b=89):
    """
    This methods adds two integers together
    """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    elif not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a or b must be an integer or float")
    return a + b
