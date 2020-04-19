#!/usr/bin/env python3
"""Example of unittest module."""

import unittest

class TestSomething(unittest.TestCase):
    """Tests for Something"""

    def setUp(self):
        """Called before each test method is run."""
        pass

    def test_something(self):
        """A unittest"""
        self.assertEqual(1, 1)

    def test_something_else(self):
        """Another unittest"""
        self.assertEqual(0, 0)

    def tearDown(self):
        """Called after each test method is run."""
        pass

if __name__ == "__main__":
    unittest.main()
