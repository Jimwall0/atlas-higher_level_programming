#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for num in range(len(my_list)):
        if idx == num:
            return my_list[num]
    return None
