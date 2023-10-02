#!/usr/bin/python3
"""
rect inherits from base
"""
from base import Base


class Rectangle(Base):
    """
    rect from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        doc, you hear
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        private getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        prop okay?
        """
        self.__width = value

    @property
    def height(self):
        """
        private getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        prop okay?
        """
        self.__height = value

    @property
    def x(self):
        """
        private getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        prop okay?
        """
        self.__x = value

    @property
    def y(self):
        """
        private getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        prop okay?
        """
        self.__width = value
