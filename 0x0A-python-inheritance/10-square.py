#!/usr/bin/python3
"""
This module is from task 9
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits class from Rectangle (9-rectangle.py)
    """

    def __init__(self, size):
        self.__size = size
        self.__width = size
        self.__height = size
        super().__init__(size, size)

    def __str__(self):
        return ("[{}] {:d}/{:d}".
                format(self.__class__.__name__,
                       self.__width,
                       self.__height))
