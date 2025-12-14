#!/usr/bin/python3
"""
wth is this
"""


def inherits_from(obj, a_class):
    """
    1. obj is instance of a_class
    2. obj is not exactly same as a_class | it inherits
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
