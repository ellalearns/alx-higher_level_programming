#!/usr/bin/python3
"""
MyInt class that inherits from int, but has inverted == and !=
"""


class MyInt(int):
    """
    not empty
    """
    def __eq__(self, other):
        if self == other:
            return False

    def __ne__(self, other):
        if self != other:
            return False
