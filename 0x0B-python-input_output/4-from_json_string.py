#!/usr/bin/python3
"""
returns json object from string
"""
import json


def from_json_string(my_str):
    """
    converts a string to json
    :param my_str: the json string
    :return: json object
    """
    return json.load(my_str)
