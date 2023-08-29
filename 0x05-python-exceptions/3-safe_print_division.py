#!/usr/bin/python3

def safe_print_division(a, b):
    """
    safely divides two integers
    :param a: first integer
    :param b: second integer
    :return: results
    """
    result = 0
    try:
        result = a / b
    except (ZeroDivisionError, ValueError):
        result = None
    finally:
        print("Inside result: {:d}".format(result))

    return result
