#!/usr/bin/python3
for x in map(chr, range(97, 123)):
    if x == 'q': continue
    if x == 'e': continue
    print("{}".format(x), end="")
