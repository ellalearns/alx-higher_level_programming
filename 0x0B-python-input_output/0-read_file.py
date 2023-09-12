#!/usr/bin/python3


def read_file(filename=""):
    """
    read a file
    :param filename: the name of file
    :return: nothing
    """
    with open(filename, "r", encoding="utf-8") as file:
        data_read = file.read()
        print(data_read)
