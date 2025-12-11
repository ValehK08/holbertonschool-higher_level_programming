#!/usr/bin/python3
"""RECTANGLEE"""


class Rectangle:
    """DEFINE IT"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.area() == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self, mes=''):
        if self.area() == 0:
            return ""
        self.mes = mes
        for i in range(self.height):
            self.mes += ('#' * self.width)
            if i != self.height - 1:
                self.mes += '\n'
        return self.mes

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
