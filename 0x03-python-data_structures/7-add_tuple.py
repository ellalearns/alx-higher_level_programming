#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """sum two tuples into one
    add the first elements of both to a new tuple
    add the second elements of both to the new tuple
    assuming all elements are integers

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        a new tuple
    """
    a_len = len(tuple_a)
    b_len = len(tuple_b)

    if a_len >= 2:
        new_a = (tuple_a[0], tuple_a[1])
    elif a_len == 1:
        new_a = (tuple_a[0], 0)
    else:
        new_a = (0, 0)

    if b_len >= 2:
        new_b = (tuple_b[0], tuple_b[1])
    elif b_len == 1:
        new_b = (tuple_b[0], 0)
    else:
        new_b = (0, 0)

    new_tuple = (new_a[0] + new_b[0], new_a[1] + new_b[1])

    return new_tuple
