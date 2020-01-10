#!/usr/bin/python3
class Square:
    """Square - a class Square that defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
            self.position = position

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

    @property
    def position(self):
        """position: Set availabilty of size to retreive it"""
        return self.__position

    @position.setter
    def position(self, value):
        """value: Get the values to set it"""
        if ((type(value) is not tuple) or
                (len(value) != 2) or
                (type(value[0]) is not int) or
                (type(value[1]) is not int) or
                (value[0] < 0) or
                (value[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """my_print - Method that prints in stdout the square with the
           character #
        """
        if self.size is 0:
            print("")
        else:
            for c in range(self.position[1]):
                print()
            for d in range(self.size):
                for a in range(self.position[0]):
                    print("{}".format(" "), end="")
                for b in range(self.size):
                    print("{}".format("#"), end="")
                print()
