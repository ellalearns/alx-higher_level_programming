#!/usr/bin/python3
"""
This file contains an empty class - Square.
"""


class Square:
    """
    This is the empty class Square
    """
    def __init__(self, size=0):
        """
        This is the initialization function
        :param size: a private instance attribute
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        area = self.__size ** 2
        return area
