#!/usr/bin/python3
"""Square - an empty class Square that defines a square"""


class Rectangle:
    """Define instantiates for the square"""
    def __init__(self, width=0, height=0):
        """Set with an height"""
        self.width = width
        self.height = height

    def __str__(self):
        """String representation
        """
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res
        for h in range(self.__height):
            for w in range(self.__width):
                res += '#'
            res += '\n'
        return res[:-1]

    def __repr__(self):
        """Eval is magic string representation
        """
        r = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return r

    @property
    def width(self):
        """return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set and validations
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set and validations
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Set area.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Set perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2