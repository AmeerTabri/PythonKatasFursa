import unittest
from katas.reduce_list import reduce_array


class TestReduceList(unittest.TestCase):
    def test1(self):
        # Original test
        self.assertEqual(reduce_array([10, 15, 7, 20, 25]), [10, 5, -8, 13, 5])
        self.assertEqual(reduce_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(reduce_array([]), [])
        self.assertEqual(reduce_array([1]), [1])
        self.assertEqual(reduce_array([5, 10]), [5, 5])
        self.assertEqual(reduce_array([-5, -10, -3]), [-5, -5, 7])
        self.assertEqual(reduce_array([3, -4, 7, -2]), [3, -7, 11, -9])
        self.assertEqual(reduce_array([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(reduce_array([1000000, 500000, 250000]), [1000000, -500000, -250000])
