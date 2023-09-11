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
        if BG.integer_validator(width):
            self.__width = width

        if BG.integer_validator(height):
            self.__height = height
