#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with string length and first character

    Args:
         sentence: the string

    Returns:
        a tuple containing sentence's length and first character
    """
    if sentence == "" or sentence is None:
        return (0, None)

    else:
        strlen = len(sentence)
        firstChar = sentence[0]

        return (strlen, firstChar)
