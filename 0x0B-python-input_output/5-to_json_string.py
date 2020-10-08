#!/usr/bin/python3
import json
"""
This is module 5-to_json_string
This module contains one function `to_json_string`
"""


def to_json_string(my_obj):
    """
    function that returns JSON representation
    of an object (string):
    """
    js = json.dumps(my_obj)
    return (js)
