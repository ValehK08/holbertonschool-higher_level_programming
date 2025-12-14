#!/usr/bin/python3
"""JSON TO STRING"""
json = __import__('json').dumps

def to_json_string(my_obj):
    """FUNCTION TO CONVERT JSON TO STRING"""

    return dumps(my_obj)
