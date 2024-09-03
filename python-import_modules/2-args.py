#!/usr/bin/python3
import sys


def main():
    total = len(sys.argv)
    if total - 1 == 0:
        print("{} arguments.".format(0))
        exit
    elif total - 1 == 1:
        print("{} argument:".format(total - 1))
    else:
        print("{} arguments:".format(total - 1))
    for x in range(1, total):
        print("{}: {}".format(x, sys.argv[x]))


if __name__ == "__main__":
    main()
