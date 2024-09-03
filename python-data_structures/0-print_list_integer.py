#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        p = "{:n}"
        print(p.format(my_list[num]))
