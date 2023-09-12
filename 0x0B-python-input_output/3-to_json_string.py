#!/usr/bin/python3
"""
returns json rep of an str obj
"""
import json


def to_json_string(my_obj):
    """
    converts a string to json
    :param my_obj: the string
    :return: json rep of string
    """
    return json.dumps(my_obj)
