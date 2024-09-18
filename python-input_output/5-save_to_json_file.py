#!/usr/bin/python3
"""
Write a function that writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes to file in json
    """

    with open(filename, "w") as file:
        file.write(json.loads(my_obj))
