#!/usr/bin/python3

def lookup(obj):
    """
    returns all the attributes and functions of a class
    :param obj: the class
    :return: list of all available attributes and functions of obj class
    """
    all_attr = dir(obj)

    return all_attr
