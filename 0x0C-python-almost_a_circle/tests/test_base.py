#!/usr/bin/python3
"""
tests for base.py
"""
import unittest
from models.base import Base



class TestBase(unittest.TestCase):
    """
    bla bla bla
    """
    def setUp(self):
        self.base1 = Base()
        self.base2 = Base(24)
        self.base3 = Base()

    def test_base_id(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 24)
        self.assertEqual(self.base3.id, 2)

if __name__ == "__main__":
    unittest.main()
