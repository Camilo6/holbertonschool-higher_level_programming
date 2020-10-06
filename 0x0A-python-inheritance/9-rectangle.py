#!/usr/bin/python3
"""This module based on task 8"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from BaseGeometry (7-base_geometry.py)."""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__height * self.__width)

    def __str__(self):
        return ("[{:s}] {:d}/{:d}".
            format(self.__class__.__name__,
                       self.__width,
                       self.__height))
