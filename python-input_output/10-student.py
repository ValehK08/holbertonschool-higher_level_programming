#!/usr/bin/python3
"""CLASS: STUDENT"""


class Student:
    """STUDENT"""

    def __init__(self, first_name, last_name, age):
        """INITIALIZE"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            if all(isinstance(i, str) for i in attrs):
                return {key: self.__dict__[key] for key in attrs}
            else:
                return self.__dict__
        else:
            return self.__dict__
