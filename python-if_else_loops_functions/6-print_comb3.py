#!/usr/bin/python3
for x in range(10):
    for i in range(1, 10):
        if i < x:
            continue
        elif i == x:
            continue
        print("{}{}".format(x, i), end=", " if x != 9 else "")
print()
