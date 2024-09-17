#!/usr/bin/python3
"""
Write a function that writes a string to
 a text file (UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):

    """
    write to a file function
    """
    with open(filename, "a") as file:
        x = file.write(text)
    return x
