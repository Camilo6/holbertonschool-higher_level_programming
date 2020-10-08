#!/usr/bin/python3
"""
This module is from task 6
"""

import json


def from_json_string(my_str):
    """
    function that returns an object
    (Python data structure) represented
    by a JSON string:
    """
    js = json.loads(my_str)
    return (js)
