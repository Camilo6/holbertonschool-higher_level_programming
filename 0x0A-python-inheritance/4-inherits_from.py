#!/usr/bin/python3
"""This module is from task 4"""


def inherits_from(obj, a_class):
    """This unction that returns True if the object
     is an instance of a class that inherited
     from the specified class ; otherwise False
    """
    return (isinstance(obj, a_class) and obj.__class__ != a_class)
