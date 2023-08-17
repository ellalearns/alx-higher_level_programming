#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns weighted average of list of tuples
    """
    if len(my_list) < 1:
        return 0
    else:
        total = 0
        product = 0
        for tup in my_list:
            product += tup[0] * tup[1]
        for tup in my_list:
            total += tup[1]

        return product / total
