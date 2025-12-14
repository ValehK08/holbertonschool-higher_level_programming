#!/usr/bin/python3
"""
Base
"""


class BaseGeometry:
    """
    GEOOOOMETRY
    """

    def area(self):
        """
        AREAAAA
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        LEET'S VALIDATE
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")