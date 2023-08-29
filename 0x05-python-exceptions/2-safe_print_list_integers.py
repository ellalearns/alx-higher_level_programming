#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only ints
    :param my_list: the list
    :param x: first x elements to print
    :return: real number of integers printed
    """
    counter = 0
    while counter < x:
        try:
            print("{:d}".format(my_list[counter]), end="")
            counter += 1
        except IndexError:
            return counter
        except (ValueError, TypeError):
            counter += 1
            pass
    print("\n")
    return counter
