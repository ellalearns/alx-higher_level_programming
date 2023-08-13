#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print reversed list of integers

    Args:
        my_list: the list

    Returns:
        null
    """
    my_list.reverse()
    for int in my_list:
        print("{:d".format(int))
