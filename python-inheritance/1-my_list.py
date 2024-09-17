#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""
class MyList(list):
    """
    This is a class containing function and list attributes
    """
    def __init__(self):
        super().__init__()
    def print_sorted(self):
        """
        This prints a sorted list
        """
        temp = self.copy()
        temp.sort()
        print(temp)
