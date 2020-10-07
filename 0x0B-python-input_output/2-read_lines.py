#!/usr/bin/python3
"""This module is from task 2"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of
    a text file (UTF8) and prints it to stdout"""
    count = 0
    with open(filename, 'r', encoding='utf-8') as fi:
        if (nb_lines <= 0):
            print(fi.read(), end="")
        else:
            for line in fi:
                if count < nb_lines:
                    print(line, end="")
                    count += 1
