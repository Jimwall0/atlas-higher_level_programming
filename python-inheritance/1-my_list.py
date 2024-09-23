#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    This is a class containing function and list attributes
    """
    def print_sorted(self):

        """
        This prints a sorted list

        >>>MyList = __import__('1-my_list').MyList
        >>>my_list = MyList()
        >>>my_list.append(1)
        >>>my_list.append(4)
        >>>my_list.append(2)
        >>>my_list.append(3)
        >>>my_list.append(5)
        >>>print(my_list)
        [1, 4, 2, 3, 5]
        my_list.print_sorted()
        [1, 2, 3, 4, 5]
        print(my_list)
        [1, 4, 2, 3, 5]
        """
        temp = self.copy()
        temp.sort()
        print(temp)
