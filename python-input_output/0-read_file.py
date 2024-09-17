#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):

    """
    This is the method to read a file
    """

    with open(filename) as file:
        print(file.read())
