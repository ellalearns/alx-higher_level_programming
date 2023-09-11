#!/usr/bin/python3
"""
square inherits from rectangle
"""
Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    """
    another doc
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
