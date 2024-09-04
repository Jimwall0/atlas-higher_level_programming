#!/usr/bin/python3
def safe_print_integer(value):
    try:
        "{:d}".format(value)

    except:
        return False
    return True