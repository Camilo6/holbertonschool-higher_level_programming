#!/usr/bin/python3
"""
This module is from task 8
"""

import json


def load_from_json_file(filename):
    """This function that creates an
    Object from a “JSON file”"""
    with open(filename, encoding='utf-8') as f:
        return (json.load(f))
