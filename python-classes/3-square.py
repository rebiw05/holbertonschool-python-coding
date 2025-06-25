#!/usr/bin/python3
"""
This is the square with propety setter.

this module represents property setter and
optional size of the square
"""


class Square:
    """
    This module represents square class.

    In this module, we will explore square
    area and property setter.
    """

    def __init__(self, size=0):
        """
        this module represents size as optinal
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return int(self.__size)**2
