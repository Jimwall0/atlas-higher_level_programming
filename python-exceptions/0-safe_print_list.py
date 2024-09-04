#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for num in range(x):
            if not my_list[num]:
                raise IndexError
            else:
                print("{}".format(my_list[num]), end="")
        print()
        return num + 1
    
    except IndexError:
        return num