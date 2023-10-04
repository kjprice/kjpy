import unittest
from src.kjpy.example import add_one


class TestExample(unittest.TestCase):
    def test_addone(self):
        self.assertEqual(add_one(1), 2)
        # self.assertEqual(average([]), 0)
