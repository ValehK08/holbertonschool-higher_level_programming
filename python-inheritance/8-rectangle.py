#!/usr/bin/python3
"""DOCUMENTATION OF ITT"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """RECTANGULATE ITTT"""

    def __init__(self, width, height):
        """INITIALIZE ITT"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
