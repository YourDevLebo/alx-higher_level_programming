#!/usr/bin/python3
""" filename - 0-add_integer.py
    define function that adds 2 integers
    Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """ return integer of a and b
        a and b must integers or float
        otherwise return TypeError
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
