#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    replaces a list element
    at an index
    with another element
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
