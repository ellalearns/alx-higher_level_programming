#!/usr/bin/python3
def print_last_digit(number):
    """
    print and return the last digit of a number
    """
    print("{}".format(int(str(number)[-1])), end="")

    return int(str(number)[-1])
