#!/usr/bin/python3
"""
prints square with # character
"""


def print_square(size):
    """
    print square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    counter = 0
    while counter < size:
        print("{}".format("#" * size))
        counter += 1
