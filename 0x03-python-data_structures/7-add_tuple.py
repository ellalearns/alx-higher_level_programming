#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds the elements of two tuples
    returns a tuple
    """
    first_int = 0
    second_int = 0
    first_int_b = 0
    second_int_b = 0

    if len(tuple_a) > 0:
        first_int = tuple_a[0]
        if len(tuple_a) > 1:
            second_int = tuple_a[1]

    if len(tuple_b) > 0:
        first_int_b = tuple_b[0]
        if len(tuple_b) > 1:
            second_int_b = tuple_b[1]

    first_arg = first_int + first_int_b
    second_arg = second_int + second_int_b

    return first_arg, second_arg
