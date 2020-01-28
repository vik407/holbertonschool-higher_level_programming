#!/usr/bin/python3
"""
Testcases for rectangle class
"""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Rectngle class tests"""

    def test_rectangle_isinstance(self):
        """isinstance."""
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test_rectangle_single(self):
        """One value"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_rectangle_none(self):
        """None"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(x.exception))

    def test_rectangle_empty(self):
        """Empty values"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(x.exception))

    def test_rectangle_strings(self):
        """string values"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, "1")
        self.assertEqual(
            "height must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle("5", 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r8 = Rectangle(10, 2, "2")
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2, 0, "Holberton")
        self.assertEqual(
            "y must be an integer",
            str(x.exception))

if __name__ == '__main__':
    unittest.main()
