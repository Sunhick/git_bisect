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
