import sys
import unittest

from main import Add

class calc(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_add(self):
        self.assertTrue(10, Add(3, 7))

if __name__ == "__main__":
    unittest.main()
