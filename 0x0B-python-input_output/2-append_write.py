#!/usr/bin/python3
"""
create file if it doesn't exist. append to it if it does.
"""


def append_write(filename="", text=""):
    """
    create or append, as it needeth to be.
    :param filename: file name and path
    :param text: text to be appended
    :return: no of chars appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        appended_data = file.write(text)

    return appended_data
