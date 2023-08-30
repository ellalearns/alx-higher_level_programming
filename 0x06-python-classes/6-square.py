#!/usr/bin/python3
"""
This file contains an empty class - Square.
"""


class Square:
    """
    This is the empty class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This is the initialization function
        :param size: a private instance attribute
        :param position: also private instance attribute
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        returns the value of size
        :return: returns size
        """
        size_gotten = self.__size
        return size_gotten

    @property
    def position(self):
        """
        returns the value of position
        :return: returns position
        """
        current_position = self.__position
        return current_position

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

    @position.setter
    def position(self, value):
        """
        sets the value of position
        :param value: the tuple to be set as position
        :return: nothing
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            current_position = self.__position
            line = "#" * current_size
            if current_position[1] == 0:
                space = 0
            else:
                space = " " * current_position[1]
            while counter < current_size:
                if current_position[1] > 0:
                    print(space, end="")
                print(line)
                counter += 1
