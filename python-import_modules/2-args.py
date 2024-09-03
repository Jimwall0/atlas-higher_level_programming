#!/usr/bin/python3
import sys


def main():
    total = len(sys.argv)
    if total == 0:
        print(".")
        exit
    for x in range(1, total):
        print("{}:{}".format(x, sys.argv[x]))

if __name__ == "__main__":
    main()