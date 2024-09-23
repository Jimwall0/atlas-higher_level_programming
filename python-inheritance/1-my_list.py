#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """This is a class containing function and list attributes

    >>> my_list = MyList()
    >>> my_list.extend([3, 1, 4, 1, 5, 9, 2, 6])
    >>> my_list.print_sorted()
    [1, 1, 2, 3, 4, 5, 6, 9]
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
