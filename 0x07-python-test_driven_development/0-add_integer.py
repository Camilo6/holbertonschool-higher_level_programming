#!/usr/bin/python3
"""This module is from task 0"""


def add_integer(a, b):
    """This function adds two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a_int = int(a)
    b_int = int(b)
    return(a_int + b_int)
