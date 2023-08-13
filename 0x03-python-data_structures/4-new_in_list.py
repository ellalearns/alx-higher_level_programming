#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """returns a new list.
    new list is a copy of old list:
    an element in the old list is replaced in the copy.

    Args:
        my_list: original list
        idx: index to replace at
        element: replacement element

    Returns:
        new list with replaced element
    """
    if type(my_list) is list:
        new_list = my_list[:]

        if idx < 0:
            return new_list

        elif idx >= len(my_list):
            return new_list

        else:
            new_list[idx] = element
            return new_list
