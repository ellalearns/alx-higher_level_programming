#!/usr/bin/python3
"""
rectangle class that inherits from BaseGeometry
"""
BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """
    rectangle subclass  class
    """

    def __init__(self, width, height):
        super().integer_validator("my_width", width)
        self.__width = width

        super().integer_validator("my_height", height)
        self.__height = height
