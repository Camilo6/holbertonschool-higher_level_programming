#!/usr/bin/python3
"""This module is from task 1"""


class MyList(list):
    """This class inherits from list"""

    def print_sorted(self):
        sorted_list = MyList()
        for item in self:
            sorted_list.append(item)
        print(sorted(sorted_list))
