#!/bin/usr/python3
"""
a MyList class that inherits from list
"""


class MyList(list):
    """
    MyList class
    """

    def print_sorted(self):
        """
        prints this sorted list in ascending order
        :return: no return
        """
        print(sorted(self))

