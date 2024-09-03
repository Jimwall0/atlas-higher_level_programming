#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    for num in range(len(my_list)):
        if num == idx:
            my_list[num] = element
    return my_list
