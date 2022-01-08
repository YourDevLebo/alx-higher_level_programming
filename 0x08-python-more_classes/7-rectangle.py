#!/usr/bin/python3
""" File name : 7-rectangle.py
    Change representation
    It is not allowed to import any module
"""


class Rectangle(object):
    """ defining new Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializing the new rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ Print the rectangle with the character # """
        rectangle = ""
        if (self.__height or self.__width) == 0:
            return rectangle
        for i in range(self.__height):
            for i in range(self.__width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        """ string representation of rectangle """
        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """Delete class rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
