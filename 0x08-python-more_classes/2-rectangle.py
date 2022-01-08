#!/usr/bin/python3
""" File name : 2-rectangle.py
    Area and Perimeter : calculate area and perimeter
    It is not allowed to import any module
"""


class Rectangle(object):
    """ defining new Rectangle class """
    def __init__(self, width=0, height=0):
        """ initializing the new rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property for attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ raise typeError if not int """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property for attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ raise typeError if not int """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """ raise ValueError if < 0 """
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ define area that returns rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ define perimeter that returns rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
