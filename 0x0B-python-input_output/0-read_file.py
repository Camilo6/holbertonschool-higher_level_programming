#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as filee:
        for line in filee:
            line = line.strip()
            print(line)