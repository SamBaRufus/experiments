# -*- coding: utf-8 -*-

"""
Tests for somelib.module
"""

import unittest

from .. import module


class TestModule(unittest.TestCase):
    
    def test_hello_world(self):
        """
        test expected value is returned
        """
        expected = 'hello world!'
        result = module.hello_world()
        self.assertEqual(expected, result)

    def test_hello_world_type(self):
        """
        test hello_world returns a string
        """
        result = module.hello_world()
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main(verbosity=2)
