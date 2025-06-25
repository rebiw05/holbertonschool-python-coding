#!/usr/bin/python3
"""
this module defines square with private optional size.

it is a foundational modul for create with private size
"""


class Square:

    """
    represents a square.

    The size is stored as a private
    instance attribute to enforce control over its type and value.

    Attributes:
        __size (int): The size of one side of the square. And must be kept
        as private
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        At this stage demonstrating a basic
        private attribute assignment.
        """
        if not isinstance(size, int):
            # Raise a TypeError if the provided size is not an integer
            raise TypeError("size must be an integer")
        if size < 0:
            # Raise a ValueError if the provided size is less than 0
            raise ValueError("size must be >= 0")
        self.__size = size
