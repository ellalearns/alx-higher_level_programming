#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """multiply all values in a dict by 2
    returns a new dict
    """
    new_dict = a_dictionary
    all_keys = sorted(a_dictionary)
    for key in all_keys:
        new_dict[key] *= 2
    return new_dict
