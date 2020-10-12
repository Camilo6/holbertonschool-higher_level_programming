#!/usr/bin/python3
"""class base"""

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if self.id != None:
            __nb_objects = self.id
        else:
            __nb_objects += 1
            self.id = __nb_objects