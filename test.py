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

from main import Add, Sub

class calc(unittest.TestCase):
    def setUp(self):
    	"""
    	Setup the test cases
    	"""
        pass

    def tearDown(self):
    	"""
    	Teardown the test cases
    	"""
        pass
    
    def test_add_true(self):
    	"""
    	Test to check if the add returns correct value
    	"""
        self.assertEqual(10, Add(3, 7))

    def test_add_false(self):
    	"""
    	Test to check if the add wont' return incorrect value
    	"""
        self.assertNotEqual(100, Add(3, 7))

    def test_sub_true(self):
        """
        test to check if sub returns correct value
        """
    	self.assertEqual(0, Sub(3, 3))

    def test_sub_false(self):
        """
        test to check if sub returns correct value
        """
        self.assertNotEqual(10, Sub(38, 38))

if __name__ == "__main__":
    unittest.main()
