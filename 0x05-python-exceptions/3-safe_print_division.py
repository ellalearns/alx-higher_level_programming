#!/usr/bin/python3

def safe_print_division(a, b):
    """
    safely prints the quotient of 2 integers
    """
    result = 0
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
