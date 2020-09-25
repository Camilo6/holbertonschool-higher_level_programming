#!/usr/bin/python3
"""This module is from task 5"""


def text_indentation(text):
    """
    This function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    to_print = ""
    characters = ['.', '?', ':']
    for string in text:
        to_print += string
        if string in characters:
            to_print += "\n\n"
            print(to_print, end='')
