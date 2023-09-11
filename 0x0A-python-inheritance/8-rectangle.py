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
        BG.integer_validator("width", width)
        self.__width = width

        BG.integer_validator("height", height)
        self.__height = height
