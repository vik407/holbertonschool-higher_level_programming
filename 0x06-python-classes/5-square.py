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

    @property
    def size(self):
        """size: Set availabilty of size to retreive it"""
        return self.__size

    @size.setter
    def size(self, value):
        """value: Get the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """my_print - Method that prints in stdout the square with the
           character #
        """
        if self.size is 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * (self.size))
