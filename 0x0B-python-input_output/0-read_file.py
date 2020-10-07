#!/usr/bin/python3
"""This module is from task 0"""


def read_file(filename=""):
    """This function prints content of a file"""
    with open(filename, 'r', encoding='utf-8') as fi:
            print(fi.read(), end="")
