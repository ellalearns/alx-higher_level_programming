#!/usr/bin/python3
"""
uses issubclass to check if an obj is a subclass of a_class
"""


def inherits_from(obj, a_class):
    """
    returns true or false if obj is a subclass of a_class
    :param obj: the object
    :param a_class: the super class
    :return true or false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    else:
        return False
