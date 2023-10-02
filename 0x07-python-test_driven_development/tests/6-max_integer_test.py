#!/usr/bin/python3
"""
oya eat the doc
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def testsuite(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)
        self.assertEqual(max_integer([1, 3, -4, 2]), 3)
        self.assertEqual(max_integer([-7, -9, -4, -8]), -4)
        self.assertEqual(max_integer([4]), 4)


if __name__ == "__main__":
    unittest.main()
