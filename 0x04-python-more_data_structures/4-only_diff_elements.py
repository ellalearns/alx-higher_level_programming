#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """set of elements present in only one set
    Args:
        set_1: first set
        set_2: second set
    Returns:
        list: elements in one set
    """
    return set_1 ^ set_2
