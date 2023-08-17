#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a roman_string to integer
    roman numeral between 1 and 3999
    """
    if type(roman_string) is not str:
        return None
    if roman_string is None:
        return None
