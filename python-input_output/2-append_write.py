#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):

    """
    writes to a function with text already in it
    """
    with open(filename, "a") as file:
        return file.write(text)
