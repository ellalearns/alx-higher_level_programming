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
        self.__size = size

    @property
    def size(self):
        """
        returns the value of size
        :return: returns size
        """
        size_gotten = self.__size
        return size_gotten

    @size.setter
    def size(self, value):
        """
        sets the size value
        :param value: the value to set size
        :return: no return
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the area of a square based on this class def
        :return: square area based on size
        """
        area = self.__size ** 2
        return area

    def my_print(self):
        """
        prints square to stdout in python
        :return: no return
        """
        if self.size == 0:
            print("")
        else:
            counter = 0
            current_size = self.size
            line = "#" * current_size
            while counter < current_size:
                print(line)
                counter += 1
