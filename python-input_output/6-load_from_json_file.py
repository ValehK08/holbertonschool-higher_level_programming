#!/usr/bin/python3
"""READ THE JSON"""
import json


def load_from_json_file(filename):
    """FUNCTION TO READ THE JSON"""

    with open(filename, 'r') as file:
        my_obj = json.load(file)

    return my_obj
