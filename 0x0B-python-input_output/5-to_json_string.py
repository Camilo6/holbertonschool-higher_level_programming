#!/usr/bin/python3
"""
This is module 5-to_json_string
This module contains one function `to_json_string`
"""

import json


def to_json_string(my_obj):
    """
    function that returns JSON representation
    of an object (string):
    """
    js = json.dumps(my_obj)
    return (js)
