#!/usr/bin/python3
"""
Testcases for base class
"""
import unittest
import os
from models import base
from models.base import Base


class BaseTest(unittest.TestCase):
    """Set the cases on this class
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_sum_id(self):
        """Sum every instantiate of the class."""
        a = Base()
        b = Base()
        c = Base()
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 3)

    def test_base_custom_id(self):
        """Custom base id"""
        a = Base(2020)
        self.assertEqual(a.id, 2020)

    def test_base_correct_id_after_custom(self):
        """No custom id"""
        a = Base()
        self.assertEqual(a.id, 1)

    def test_base_string(self):
        """String id"""
        a = Base("Holberton")
        self.assertEqual(a.id, "Holberton")

    def test_base_none(self):
        """None id"""
        a = Base(None)
        self.assertEqual(a.id, 1)

    def test_base_zero(self):
        """Zero id"""
        a = Base(0)
        self.assertEqual(a.id, 0)

    def test_base_negative(self):
        """Test for negative input."""
        a = Base(-1)
        self.assertEqual(a.id, -1)

    def test_base_list(self):
        """Test for list input."""
        a = Base([1, 2, 3])
        self.assertEqual(a.id, [1, 2, 3])

    def test_base_dict_kv(self):
        """Key value dict"""
        a = Base({"Holberton": "School"})
        self.assertEqual(a.id, {"Holberton": "School"})

    def test_09_float(self):
        """Float"""
        a = Base(0.1)
        self.assertEqual(a.id, 0.1)

    def test_base_tuple(self):
        """Test for tuple input."""
        a = Base((1,))
        self.assertEqual(a.id, (1,))

if __name__ == '__main__':
    unittest.main()
