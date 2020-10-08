#!/usr/bin/python3
"""
This module is from task 5
"""

import json


def to_json_string(my_obj):
    """
    function that returns JSON representation
    of an object (string):
    """
    js = json.dumps(my_obj)
    return (js)
