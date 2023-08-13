#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replace a list element at a given index

    Args:
        my_list: the list
        idx: the index
        element: the replacement element

    Returns:
        modified list
    """
    if idx < 0:
        return my_list

    elif idx >= len(my_list):
        return my_list

    else:
        my_list[idx] = element
        return my_list
