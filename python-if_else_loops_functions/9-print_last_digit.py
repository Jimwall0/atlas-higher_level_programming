#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if n < 0:
        n * -1
    print("{}".format(number % 10), end="")
    return number % 10
