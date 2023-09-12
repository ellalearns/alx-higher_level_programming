#!/usr/bin/python3
"""
load a json obj from file
"""
import json


def load_from_json_file(filename):
    """
    load json obj from txt file
    :param filename: the file to load from
    :return: nothing
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.load(file)
