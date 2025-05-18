#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([13, 42, 4, 50]), 50)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-89, 0, -20, -40]), 0)
        self.assertEqual(max_integer([50]), 50)
        self.assertEqual(max_integer([]), None)

    def test_max_boolean(self):
        self.assertTrue(max_integer([True, False]), True)

    def test_max_string(self):
        self.assertEqual(max_integer(["tuwaiq"]), "tuwaiq")
