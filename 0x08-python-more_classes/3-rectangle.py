#!/usr/bin/python3
"""
This module is for task 3
"""


class Rectangle:
    """
    This class defines a rectangle based on 2-rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return((self.__height * 2) + (self.width * 2))

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            pubheight = self.__height
            pubwidth = self.__width
            string = ''.join(('#' * pubwidth + '\n') * pubheight)
            string = string[0:-1]
            return (string)
