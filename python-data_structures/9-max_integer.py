#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or my_list is None:
        return None
    max = 0
    for loop in my_list:
        if my_list[loop] > max:
            max = my_list[loop]
    return max
