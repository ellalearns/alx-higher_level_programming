#!/usr/bin/python3
"""
MyInt class that inherits from int, but has inverted == and !=
"""


class MyInt(int):
    """
    not empty
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
