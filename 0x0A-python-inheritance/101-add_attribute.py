#!/usr/bin/python3
"""
adds a new attribute to an object if possible
"""


def add_attribute(class_ins, attr_name, attr_value):
    """
    adds a new attribute to an obj if possible
    :param class_ins: obj instance of class
    :param attr_name: name of attribute
    :param attr_value: value of attribute
    :return: obj class
    """
    if type(class_ins) is str or type(class_ins) is int:
        raise TypeError("can't add new attribute")

    if type(class_ins) is tuple:
        raise TypeError("can't add new attribute")

    if type(class_ins) is float or type(class_ins) is None:
        raise TypeError("can't add new attribute")

    if not hasattr(class_ins, attr_name):
        raise TypeError("can't add new attribute")

    if hasattr(class_ins, attr_name):
        raise TypeError("can't add new attribute")

    if not hasattr(class_ins, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(class_ins, attr_name, attr_value)

    return class_ins
