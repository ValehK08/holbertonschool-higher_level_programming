#!/usr/bin/python3
"""
Base
"""
from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle : Inherited BaseGeometry
    """

    def __init__(self, width, height):
        """INITIALIZE"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
