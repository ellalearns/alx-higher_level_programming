#!/usr/bin/python3
def islower(c):
    """
    returns true if c is lowercase or false otherwise
    """
    if ord(c) >= 97 and ord(c) <= 123:
        return True
    else:
        return False
