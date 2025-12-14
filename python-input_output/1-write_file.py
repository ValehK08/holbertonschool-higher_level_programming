#!/usr/bin/python3
"""WRITE FILE"""


def write_file(filename="", text=""):
    """FUNCTION TO WRITE FILE"""

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in f:
            return f.write(text)
