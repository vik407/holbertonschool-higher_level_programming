#!/usr/bin/python3
"""
Square test file
"""
import sys
import os
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTest(unittest.TestCase):
    """Square tests"""

    def test_square_single_value(self):
        """One value"""
        s = Square(5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_two_values(self):
        """Two values"""
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

    def test_square_empty(self):
        """Empty"""
        with self.assertRaises(TypeError) as x:
            r = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(x.exception))

if __name__ == '__main__':
    unittest.main()
