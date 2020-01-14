#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])
    """

    def cases(self):
        '''Float test'''
        self.assertEqual([1, 2.3, 3, 4], 4)
        self.assertEqual([1, 2, 3, 4], 4)
        self.assertEqual([-1, -2, -3, -4], -1)
        self.assertEqual([4, 3, 2, 1], 4)
        self.assertEqual([-4, -3, -2, -1], -1)
        self.assertEqual([10], 10)
        self.assertEqual([], None)

if __name__ == '__main__':
    unittest.main()
