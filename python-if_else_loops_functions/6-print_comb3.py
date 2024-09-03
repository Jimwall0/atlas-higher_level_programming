#!/usr/bin/python3
for x in range(10):
    for i in range(10):
        if i < x:
            continue
        print("{}{}".format(x, i), end=", " if i != 10 else "")
print()
