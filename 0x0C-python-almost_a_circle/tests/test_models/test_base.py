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

    def test_doc(self):
        """Check for module documentation"""
        self.assertTrue(len(base.__doc__) > 0)
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.__init__.__doc__) > 0)

    def test_base_sum_id(self):
            """Sum every instantiate of the class."""
            a = Base()
            b = Base()
            c = Base()
            self.assertEqual(a.id, 1)
            self.assertEqual(b.id, 2)
            self.assertEqual(c.id, 3)
