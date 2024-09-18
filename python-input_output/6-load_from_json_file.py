#!/usr/bin/python3
"""
Write a function that creates an
Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Grabs a json and makes an object
    """

    with open(filename, "r") as file:
        json.loads(file.read())
