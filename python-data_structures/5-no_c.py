#!/usr/bin/python3
def no_c(my_string):
    copy = str(my_string)
    table = str.maketrans("", "", "cC")
    return copy.translate(table)
