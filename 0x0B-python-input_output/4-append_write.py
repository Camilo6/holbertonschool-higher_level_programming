#!/usr/bin/python3
"""This module is from task 3"""


def append_write(filename="", text=""):
    """function that writes a string to
    a text file (UTF8) and returns the
    number of characters written"""
    with open(filename, 'a', encoding='utf-8') as f:
        char_count = f.write(text)
        return (char_count)
