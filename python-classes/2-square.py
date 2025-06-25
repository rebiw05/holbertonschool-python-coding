#!/usr/bin/python3
"""
this module show that square and its area.
"""


class Square:
    """
    This class show square with optional size.

    At this stage, we will explore square optional
    size and its area

    Attributes:
        __size (int): private size
    """

    def __init__(self, size=0):
        """
        Initialize the square with an optional size.

        args:
            size (int, optional): The size of the side of the square.
        raises:
            TypeError: if it is not integer
            ValueError: if it is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        this is the area of the square

        in this stage we try to find the area
        of the square
        """
        return int(self.__size)*int(self.__size)
