#!/usr/bin/python3
"""
save an object to text file in json rep
"""
import json


def save_to_json(my_obj, filename):
    """
    write obj to txt file in json representation
    :param my_obj: the object
    :param filename: the file to write to
    :return: nothing
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
