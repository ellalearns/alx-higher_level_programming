#!/usr/bin/python3
"""
prints ascii alphabet in lowercase
"""

for str_letter in range(97, 123):
    if (chr(str_letter) != 'e' and chr(str_letter) != 'q'):
        print("{}".format(chr(str_letter)), end="")
