#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 2-square.py)
"""Area of a square: """

class Square(object):
    """class variable size"""
    def __init__(self, size=0):
        """initialize size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Define area"""
        return self.__size * self.__size
