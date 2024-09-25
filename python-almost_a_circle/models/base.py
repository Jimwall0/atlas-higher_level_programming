#!/usr/bin/python3
"""
File holding base class
"""
import json


class Base:
    """
    A base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == "" or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        if list_objs is None or list_objs == 0:
            list_objs = []
        else:
            list_objs = [item.to_dictionary() for item in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        if json_string == 0 or json_string is None:
            return []
        return json.loads(json_string)
