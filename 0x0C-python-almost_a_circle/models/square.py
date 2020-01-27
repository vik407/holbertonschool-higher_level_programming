#!/usr/bin/python3
"""
10. And now, the Square!
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Write the class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The overloading __str__ method should return [Square] (<id>) <x>/<y>
           - <size> - in our case, width or height
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
