#!/usr/bin/python3

def multiple_returns(sentence):
    """
    returns a tuple with the length of a string
    and its first character
    """
    if sentence is None or sentence == "":
        len_sen = 0
        first_char = None
    else:
        len_sen = len(sentence)
        first_char = sentence[0]
    return len_sen, first_char
