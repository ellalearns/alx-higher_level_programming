#!/usr/bin/python3
"""
tests for rect
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """
        more docs inu fdr dfgr go
        """
        self.rect1 = Rectangle(4, 6)
        self.rect2 = Rectangle(2, 1)
        self.rect3 = Rectangle(1, 3, 1, 4, 5)

    def width(self):
        """
        you want docs? chop them.
        :return:
        """
        self.assertEqual(self.rect1.width, 4)
        self.assertEqual(self.rect2.width, 2)
        self.assertEqual(self.rect3.width, 1)
        self.rect2.width(7)
        self.assertEqual(self.rect2.width, 7)


if __name__ == "__main__":
    unittest.main()
