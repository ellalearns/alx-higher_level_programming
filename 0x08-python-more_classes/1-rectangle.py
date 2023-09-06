#!/usr/bin/python3

"""
rectangle class
"""


class Rectangle:
    """
    defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initializes class Rectangle
        :param width: optional, defaults to 0
        :param height: optional, defaults to 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        gets the private width property
        :return: width
        """
        width = self.__width
        return width

    @width.setter
    def width(self, value):
        """
        set the private width property
        :param value: int value
        :return: no return value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        retrieves the private variable
        :return: height value
        """
        height = self.__height
        return height

    @height.setter
    def height(self, value):
        """
        sets the height variable
        :param value: int value
        :return: no return value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
