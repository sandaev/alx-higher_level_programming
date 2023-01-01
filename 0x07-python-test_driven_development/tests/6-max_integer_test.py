#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Child of unittest' TestCase class"""
    def test_type(self):
        """Tests for argument type"""
        lst = {1: 2, 3: 4, 5: 6}
        self.assertNotIsInstance(lst, list)

    def test_empty(self):
        """Test for empty list arg"""
        self.assertIsNone(max_integer([]))

    def test_list_elem(self):
        """Test eleme type"""
        lst = ['1', 2, 'we', 8, '3']
        with self.assertRaises(TypeError):
            max_integer(lst)



