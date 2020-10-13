#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initilize constructor with attributes'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''string representation of an instance'''
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.height)

    @property
    def size(self):
        '''getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size attribute'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['x'] = self.x
        new_dict['size'] = self.size
        new_dict['y'] = self.y
        return new_dict
