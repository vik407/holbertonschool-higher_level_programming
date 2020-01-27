#!/usr/bin/python3
"""This is the main file for the rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class for Holberton's 0x0C. Python - Almost a circle project
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance.
        """
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)


    def update(self, *args, **kwargs):
        """Adding the public method def update(self, *args): that assigns an
        argument to each attribute: id, width, height, x, y.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
