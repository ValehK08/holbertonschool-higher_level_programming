#!/usr/bin/python3
"""SAVE THE JSON AS TXT"""
import json


def save_to_json_file(my_obj, filename):
    """FUNCTION TO SAVE THE JSON AS TXT"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
