#!/usr/bin/python3
"""
base geometry class with area function
"""


class BaseGeometry:
    """
    at this point, area function
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        return True
