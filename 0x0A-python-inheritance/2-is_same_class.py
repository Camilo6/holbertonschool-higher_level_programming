#!/usr/bin/python3
"""This module is from task 2"""


def is_same_class(obj, a_class):
    """This function  that returns True
    if the object is exactly an instance
    of the specified class ; otherwise False.
    """
    return (obj.__class__ is a_class)
