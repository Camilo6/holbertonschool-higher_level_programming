#!/usr/bin/python3
"""This module is from task 15"""


def append_after(filename="", search_string="", new_string=""):
    """This function that inserts a line of text
    to a file, after each line containing
    a specific string (see example)"""
    with open(filename, 'r', encoding='utf-8') as f:
        tmp = f.readlines()
    with open(filename, 'w', encoding='utf-8') as f:
        for line in tmp:
            if line.startswith(search_string):
                line = line + new_string
            f.write(line)
