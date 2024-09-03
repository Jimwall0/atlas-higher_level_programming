#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for x in str:
        print("{}".format(chr(ord(x) - 32) if islower(x) else x), end="")
    print()
