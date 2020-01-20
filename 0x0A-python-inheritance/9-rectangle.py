#!/usr/bin/python3
"""9. Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Instantiation with width and height
           width and height must be private. No getter or setter
           width and height must be positive integers, validated
           by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Definition of area method"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
