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

    @property
    def size(self):
        """Size getter
        """
        return self.width

    @size.setter
    def size(self, size):
        """Size setter
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """adding the public method def update(self, *args, **kwargs) that
        assigns attributes: id, size, x, y.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Adding the public method def to_dictionary(self): that returns the
        dictionary representation of a Square: id, size, x, y
        """
        dict = {}
        for key, value in vars(self).items():
            if key.startswith("_"):
                if not key.endswith("width") and not key.endswith("height"):
                    idx = key.index("__")
                    dict[key[idx + 2:]] = value
                else:
                    dict["size"] = value
            else:
                dict[key] = value
        return dict
