#!/usr/bin/python3
"""READ FILE"""


def read_file(filename=""):
    """FUNCTION TO READ FILE"""

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
