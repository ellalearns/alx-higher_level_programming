#!/usr/bin/python3
"""
a function that adds integers
"""


def add_integer(a, b=98):
    """
    adds two integers

    param a: first integer
    param b: second integer

    Return: an integer
    """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return int(a + b)
