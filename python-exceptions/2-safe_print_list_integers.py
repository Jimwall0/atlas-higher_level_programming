#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for loop in range(x):
            if isinstance(my_list[loop], int):
                print("{:d}".format(my_list[loop]), end="")
                count += 1

    except IndexError:
        return count
    print()
    return count
