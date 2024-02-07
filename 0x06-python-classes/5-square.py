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

    @property
    def size(self):
        """
        retrieve size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if (isinstance(value, int)):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        returns area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints square with # character
        """
        if self.__size == 0:
            print("")
        else:
            counter = 0
            while counter < self.__size:
                for i in range(self.__size):
                    print("#", end="")
                print("")
                counter += 1
