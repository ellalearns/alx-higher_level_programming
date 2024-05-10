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
        current = nlist[count]
        prev = nlist[count - 1]
        if count >= len(nlist) - 1:
            next = nlist[count]
        else:
            next = nlist[count + 1]

        if current >= prev and current >= next:
            peaks.append(current)
            count += 2
        else:
            count += 1

    if peaks.__len__() == 1:
        return peaks[0]
    else:
        max = peaks[0]
        count = 0
        while count < len(peaks):
            if peaks[count] > max:
                max = peaks[count]
            count += 1
        return max
