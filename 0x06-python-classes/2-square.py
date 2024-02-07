#!/usr/bin/python3
"""
contains an empty class square
"""


class Square:
    """
    my new square class
    """
    def __init__(self, size=0):
        if (isinstance(size, int)):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
