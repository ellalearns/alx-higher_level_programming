#!/usr/bin/python3

def no_c(my_string):
    """
    removes all characters c and C from string
    """
    new_string = ""
    for char in my_string:
        if char == "c" or char == "C":
            pass
        else:
            new_string += char

    return new_string
