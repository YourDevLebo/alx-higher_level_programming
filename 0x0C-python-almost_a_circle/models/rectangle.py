#!/usr/bin/python3
# rectangle.py
# Lebogang Modise <djlebzana@gmail.com>
"""Define Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle: Class define rectangle
    Args:
        Base (class): parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ initialized constuctor
        Args:
            width (int)
            height (int)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        """ assigning to the right attribute """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """__str__ print information for rectangle
        Returns:
            [str]: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

