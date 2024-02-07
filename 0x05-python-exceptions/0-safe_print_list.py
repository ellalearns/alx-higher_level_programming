#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    safely print the elements of a list
    """
    counter = 0
    while counter < x:
        try:
            print(my_list[counter], end="")
            counter += 1
        except Exception:
            break
    print("")
    return counter
