#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieve the element at an index.

    Args:
        my_list: the list
        idx: the index to retrieve element from

    Returns:
        the element at given index
    """
    if idx < 0:
        return None

    elif idx >= len(my_list):
        return None

    else:
        return my_list[idx]
