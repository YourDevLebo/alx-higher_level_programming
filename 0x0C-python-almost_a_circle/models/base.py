#!/usr/bin/python3
# base.py
# Lebogang Modise <djlebzana@gmail.com>
"""Define Base class"""
import json
from os import path


class Base(object):
    """Base: Class define base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ initialized constructor
        Args:
            id (int): Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
