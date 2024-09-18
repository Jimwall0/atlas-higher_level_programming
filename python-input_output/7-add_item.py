#!/usr/bin/python3
"""
Write a script that adds all arguments to a
Python list, and then save them to a file
"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


my_list = []
if len(sys.argv) < 2:
    print("Less then 2 arg")
    exit()
for size in range(1, len(sys.argv)):
    my_list.append(sys.argv[size])
save_to_json_file(my_list, "add_item.json")
