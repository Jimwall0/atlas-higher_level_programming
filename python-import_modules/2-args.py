#!/usr/bin/python3
import sys


def main():
    total = len(sys.argv)
    print("{}:{}".format(total, sys.argv[1]))

if __name__ == "__main__":
    main()