#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return list(my_list)
    copy = list(my_list)
    for num in range(len(l)):
        if idx == num:
            copy[num] = element
    return copy
