import unittest
from katas.list_diff import find_difference

class TestListDiff(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)
        self.assertEqual(find_difference([10, 20, -10, 6, -2]), 30)
        self.assertEqual(find_difference([10]), 0)
        self.assertEqual(find_difference([1,1,1,1,1,1]), 0)
        self.assertEqual(find_difference([2**10,0,-2**10]), 2**11)
