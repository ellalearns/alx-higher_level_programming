#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only ints
    :param my_list: the list
    :param x: first x elements to print
    :return: real number of integers printed
    """
    counter = 0
    final_counter = 0
    while counter < x:
        try:
            print("{:d}".format(my_list[counter]), end="")
            counter += 1
            final_counter += 1
        except (ValueError, TypeError):
            counter += 1
            pass
    print("", end="\n")
    return final_counter
