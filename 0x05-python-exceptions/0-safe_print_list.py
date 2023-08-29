#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints the first x elements in a list
    :param my_list: the list
    :param x: the number of elements to print
    :return: real number of elements printed
    """
    counter = 0
    while counter < x:
        try:
            print(my_list[counter], end="")
            counter += 1
        except IndexError:
            print("", end="\n")
            return counter
    print("", end="\n")
    return counter
