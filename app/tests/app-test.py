import unittest
from app.src.app import my_sum

class MyTest(unittest.TestCase):
    """my_sum function Unit tests"""
    def test_my_sum(self):
        """Assert"""
        self.assertEqual(my_sum(1, 1), 2)
        self.assertEqual(my_sum(1, -1), 0)
        self.assertEqual(my_sum(0, 0), 0)
        self.assertEqual(my_sum(-1, -1), -2)
        self.assertEqual(my_sum(1.0, 1), 2)        
        self.assertEqual(my_sum(1.1, 1.1), 2.2)


if __name__ == '__main__':
    unittest.main()
