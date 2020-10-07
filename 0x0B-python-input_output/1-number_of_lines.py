#!/usr/bin/python3
"""This module is from task 1"""


def number_of_lines(filename=""):
    """This function prints number of line of a file"""
    with open(filename, 'r', encoding='utf-8') as fi:
        count = 0
        for line in fi:
            count += 1
    return(count)