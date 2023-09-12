#!/usr/bin/python3
"""
write to file. return no of chars.
"""


def write_file(filename="", text=""):
    """
    write to file. return no of characters in file.
    :param filename: file name and path
    :param text: the text to write
    :return: no of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        written_data = file.write(text)

    return written_data
