#!/usr/bin/python3
"""
Write a script that adds all arguments to a
Python list, and then save them to a file
"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def arg_add_list(file_name):
    """
    adds arguements to a list then to file
    """

    if range(sys.argv) < 2:
        print("Less then 2 arg")
        exit
    my_list = []
    for size in range(len(sys.argv), 1):
        my_list.append(sys.argv[size])
    save_to_json_file(my_list, file_name)
