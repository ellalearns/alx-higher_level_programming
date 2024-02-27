#!/usr/bin/python3

"""
function add_integer that adds two integers
"""

def add_integer(a, b=98):
    """
    adds two integers
    """
    if isinstance(a, int) is not True and isinstance(a, float) is not True:
        raise TypeError("a must be an integer")

    if isinstance(b, int) is not True and isinstance(b, float) is not True:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
