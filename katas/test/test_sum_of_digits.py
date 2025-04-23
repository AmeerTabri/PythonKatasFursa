import unittest
from katas.sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_of_digits("abc123"), 6)
        self.assertEqual(sum_of_digits("abcdef"), 0)
        self.assertEqual(sum_of_digits("1234567890"), 45)
        self.assertEqual(sum_of_digits("1a!2@3#"), 6)
        self.assertEqual(sum_of_digits("x5x"), 5)
        self.assertEqual(sum_of_digits(""), 0)
        self.assertEqual(sum_of_digits("111"), 3)
        # self.assertEqual(sum_of_digits("abc１２３"), 0)


if __name__ == "__main__":
    unittest.main()
