#!/usr/bin/python3
"""
MyInt class that inherits from int, but has inverted == and !=
"""


class MyInt(int):
    """
    not empty
    """
    def __eq__(self, other):
        result = super().__ne__(other)
        return result

    def __ne__(self, other):
        result = super().__eq__(other)
        return result
