#!/usr/bin/python

"""
	Unit testing for the functions in main
"""

__author__ = "Sunil"
__copyright__ = "Copyright 2015"
__license__ = "GNU License"
__version__ = "0.1.0"
__email__ = "suba5417@colorado.edu"

import sys
import unittest

from main import Add

class calc(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_add_true(self):
        self.assertEqual(10, Add(3, 7))

    def test_add_false(self):
        self.assertNotEqual(100, Add(3, 7))


if __name__ == "__main__":
    unittest.main()
