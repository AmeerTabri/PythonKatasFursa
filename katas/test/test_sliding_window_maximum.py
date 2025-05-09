import unittest
from katas.sliding_window_maximum import max_sliding_window


class TestSlidingWindowMaximum(unittest.TestCase):
    def test1(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        expected = [3,3,5,5,6,7]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test2(self):
        nums = [4, 2, 12, 3]
        k = 1
        expected = [4, 2, 12, 3]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test3(self):
        nums = [1, 3, 2]
        k = 3
        expected = [3]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test4(self):
        nums = [5, 5, 5, 5]
        k = 2
        expected = [5, 5, 5]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test5(self):
        nums = [9, 8, 7, 6, 5]
        k = 3
        expected = [9, 8, 7]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test6(self):
        nums = [10, 20, 30]
        k = 3
        expected = [30]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test7(self):
        nums = [42]
        k = 1
        expected = [42]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test8(self):
        nums = [1, 2]
        k = 3
        expected = []
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test9(self):
        nums = []
        k = 3
        expected = []
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test10(self):
        nums = [9, 10, 9, -7, -4, -8, 2, -6]
        k = 5
        expected = [10, 10, 9, 2]
        self.assertEqual(max_sliding_window(nums, k), expected)
