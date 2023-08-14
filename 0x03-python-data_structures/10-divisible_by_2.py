#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """returns new list containing true and false
    depending on whether each element is divisible by 2

    Args:
        my_list: original list

    Returns:
        new list
    """
    if len(my_list) == 0 or my_list is None or type(my_list) is not list:
        return None

    else:
        new_list = [True if int % 2 == 0 else False for int in my_list]

        return new_list
