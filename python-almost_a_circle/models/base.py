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
        copy = list_objs[:]
        for item in copy:
            item = cls.to_dictionary(item)
        with open(cls.__name__, "w") as file:
            file.write(cls.to_json_string(copy))
