#!/usr/bin/python3
"""11. Square #2
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Write a class Square that inherits from Rectangle (9-rectangle.py):
    """

    def __init__(self, size):
        """size must be private. No getter or setter
           size must be a positive integer, validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """the area() method must be implemented
        """
        return self.__size ** 2

    def __str__(self):
            """print() should print, and str() should return, the square
            description: [Square] <width>/<height>"""
            return "[Square] " + str(self.__size) + "/" + str(self.__size)
