#!/usr/bin/python3
class Square:
    """Square - a class Square that defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
