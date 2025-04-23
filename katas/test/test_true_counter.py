import unittest
from katas.true_counter import count_true_values


class TestTrueCounter(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)
        self.assertEqual(count_true_values([True, True, True, True, True]), 5)
        self.assertEqual(count_true_values([False, False, False, False, False]), 0)
        self.assertEqual(count_true_values([]), 0)
        self.assertEqual(count_true_values([True] * 1000), 1000)
        self.assertEqual(count_true_values([False] * 1000), 0)
        self.assertEqual(count_true_values([True, False] * 1000), 1000)


