#!/usr/bin/python3

class Square:

    """
    Represents a square.

    This class defines a square by its size. The size is stored as a private
    instance attribute to enforce control over its type and value, which
    is crucial for accurate calculations like area.

    Attributes:
        __size (int): The size of a side of the square. It's private to
                      ensure data integrity and validation through
                      controlled access (will be implemented in todo tasks).
    """

    def __init__(self, size):

        """
        Initializes a new Square instance.

        This constructor sets the size of the square. At this stage, no
        type or value verification is performed, demonstrating a basic
        private attribute assignment.

        Args:
            size (int): The size of the side of the square.
        """
        self.__size = size
