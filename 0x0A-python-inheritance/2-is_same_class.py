#!/usr/bin/python3
"""
uses isinstance to check subclass
"""


def is_same_class(obj, a_class):
    """
    returns true or false if obj is a sub of a_class
    :param obj: the object
    :param a_class: the object
    :return true or false
    """
    if type(obj) is a_class:
        return True

    else:
        return False
