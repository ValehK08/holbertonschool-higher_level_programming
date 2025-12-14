#!/usr/bin/python3
"""PASCAL"""


def pascal_triangle(n):
    """DOCUMENTED FUNCTION"""
    init = [[1]]
    if n > 1:
        init.append([1, 1])
    for i in range(2, n):
        nxt = [1]
        for k in range(i - 1):
            nxt.append(init[i-1][k] + init[i-1][k+1])
        nxt.append(1)
        init.append(nxt)
