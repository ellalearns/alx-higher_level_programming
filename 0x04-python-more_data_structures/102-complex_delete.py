#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes all keys with specific value
    """
    all_keys = sorted(a_dictionary)
    for key in all_keys:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
