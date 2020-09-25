#!/usr/bin/python3
"""
This module is from task 3
"""


def say_my_name(first_name, last_name=""):
    """This function print "My name is" follow arguments """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is: {:s} {:s}".format(first_name, last_name))
