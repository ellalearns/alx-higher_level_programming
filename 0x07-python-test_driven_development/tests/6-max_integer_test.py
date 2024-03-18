#!/usr/bin/python3

"""
a unittest module to test a function
"""


import unittest


class TestMaxInteger(unittest.TestCase):
    """
    test max integer
    """

    def setUp(self):
        self.max_integer = __import__("6-max_integer").max_integer

    def test_max(self):
        self.assertEqual(self.max_integer([]), None)
        self.assertEqual(self.max_integer([3, 5, 9, 5]), 9)
        self.assertEqual(self.max_integer([2]), 2)
        self.assertEqual(self.max_integer([-3, 0, -1]), 0)
        self.assertEqual(self.max_integer([3, 5, 5, 9]), 9)
        self.assertEqual(self.max_integer([39, 5, 9, 5]), 39)
