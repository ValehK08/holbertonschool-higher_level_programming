#!/usr/bin/python3
"""APPEND WRITE FILE"""


def append_write(filename="", text=""):
    """FUNCTION TO APPEND WRITE FILE"""

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
