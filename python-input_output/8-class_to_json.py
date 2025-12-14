#!/usr/bin/python3
"""CLASS TO JSON"""


def class_to_json(obj):
    """FUNCTION TO CONVERT CLASS TO JSON"""

    return obj.__dict__.copy()
