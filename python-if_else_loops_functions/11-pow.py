#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        number = float(1 / a)
        for loop in range (b - 1):
            number *= number
        return number
    for loop in range (b - 1):
        number *= number
    return number
    