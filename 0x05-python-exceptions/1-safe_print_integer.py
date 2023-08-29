#!/usr/bin/python3

def safe_print_integer(value):
    """
    safely print an integer
    :param value: the integer
    :return: true or false
    """
    try:
        print("{:d}".format(value), end="\n")
    except (TypeError, ValueError):
        return False
    return True
