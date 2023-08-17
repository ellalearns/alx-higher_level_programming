#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """updates a dict
    replaces if key exists
    adds if it doesn't
    """
    a_dictionary[key] = value
    return a_dictionary
