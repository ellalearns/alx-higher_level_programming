#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """delete item at a given index in a list

    Args:
        my_list: list
        idx: index

    Returns:
        modified list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    else:
        del my_list[idx]
        return my_list
