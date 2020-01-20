#!/usr/bin/python3
"""5. Geometry module, 6. Improve Geometry
"""


class BaseGeometry:
    """A class BaseGeometry."""
    def area(self):
        """Write a class BaseGeometry (based on 5-base_geometry.py).
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if is ann integer greater than 0."""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
