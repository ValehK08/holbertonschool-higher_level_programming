#!/usr/bin/python3
"""DOCUMENTATION OF ITT"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """SQUAAAAAAARE IT"""

    def __init__(self, size):
        """VALIDATE ITT"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
