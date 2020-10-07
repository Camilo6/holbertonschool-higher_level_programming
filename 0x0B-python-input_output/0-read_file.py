#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as fi:
        for line in fi:
            print(line, end="")