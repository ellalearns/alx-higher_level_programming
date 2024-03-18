#!/usr/bin/python3

"""
prints square with symbol #
"""


def print_square(size):
    """
    prints square with a symbol #
    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(int(size)):
        print("#" * int(size))
