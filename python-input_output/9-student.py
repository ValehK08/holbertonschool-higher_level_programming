#!/usr/bin/python3
"""CLASS: STUDENT"""


class Student:
    """STUDENT"""

    def __init__(self, first_name, last_name, age):
        """INITIALIZE"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
