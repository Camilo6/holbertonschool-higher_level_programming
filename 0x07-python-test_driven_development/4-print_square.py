#!/usr/bin/python3
""" This module is from task 4"""


def print_square(size):
    """This function that prints a square with the character #"""
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size == 0:
        return
    else:
        i = 0
        for i in range(0, size):
            j = 0
            for j in range(0, size):
                print('#', end="")
            print()
