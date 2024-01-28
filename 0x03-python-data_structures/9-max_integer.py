#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    returns the max integer in a list
    """
    if my_list is None:
        return None
    if len(my_list) == 0:
        return None

    max_int = my_list[0]

    for inte in my_list:
        if inte > max_int:
            max_int = inte

    return max_int
