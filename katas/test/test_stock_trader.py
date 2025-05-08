import unittest
from katas.stock_trader import max_profit


class TestStockTrader(unittest.TestCase):
    def test1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)

    def test2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)

    def test3(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)

    def test4(self):
        prices = [3, 3, 3, 3]
        self.assertEqual(max_profit(prices), 0)

    def test5(self):
        prices = []
        self.assertEqual(max_profit(prices), 0)

    def test6(self):
        prices = [9, 2, 7, 1, 6, 3]
        self.assertEqual(max_profit(prices), 5)

    def test7(self):
        prices = [5, 11, 3, 50, 60, 90]
        self.assertEqual(max_profit(prices), 87)