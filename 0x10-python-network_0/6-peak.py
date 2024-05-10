#!/usr/bin/python3
"""
checks the peak(s) in an unsorted list of integers
"""


def find_peak(list_of_integers=[]):
    """
    returns the peak(s) in an unsorted list of integers
    """
    count = 0
    peaks = []
    nlist = list_of_integers[:]
    len_list = len(nlist)

    if (len_list == 0):
        return None

    while (count < len_list):
        if nlist[count] > nlist[count - 1] and nlist[count] > nlist[count + 1]:
            peaks.append(nlist[count])
            count += 2
        else:
            count += 1

    if nlist.__len__() == 1:
        return nlist[0]
    else:
        return nlist
