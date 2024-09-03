#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in range(len(my_list) - 1, -1, -1):
        form = "{:d}"
        print(form.format(my_list[num]))
