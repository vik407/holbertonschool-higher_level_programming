#!/usr/bin/python3
"""This is the main file for the rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class for Holberton's 0x0C. Python - Almost a circle project
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
