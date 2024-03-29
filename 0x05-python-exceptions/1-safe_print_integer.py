#!/usr/bin/python3

def safe_print_integer(value):
    """
    safely prints an integer
    """
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    return True
