#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])
    """

    def test_cases_1(self):
        self.assertEqual(max_integer(), None)

    def test_cases_2(self):
        self.assertEqual(max_integer([1, 2, 0x3b76, 4]), 15222)

    def test_cases_3(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_cases_4(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_cases_5(self):
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_cases_6(self):
        self.assertEqual(max_integer([10]), 10)

    def test_cases_7(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
