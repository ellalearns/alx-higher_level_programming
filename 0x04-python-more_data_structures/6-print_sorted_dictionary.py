#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints sorted dictionary
    sorted in order of keys
    """
    s_keys = sorted(a_dictionary)

    for key in s_keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
