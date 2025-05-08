import unittest
from katas.stock_trader_v2 import max_profit


class TestStockTrader(unittest.TestCase):
    def test1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 7)

    def test2(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)

    def test3(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)

    def test4(self):
        prices = [1, 2, 1, 2, 1, 2]
        self.assertEqual(max_profit(prices), 3)

    def test5(self):
        prices = [2, 4, 1, 7]
        self.assertEqual(max_profit(prices), 8)

    def test6(self):
        prices = []
        self.assertEqual(max_profit(prices), 0)

    def test7(self):
        prices = [5]
        self.assertEqual(max_profit(prices), 0)

    def test10(self):
        prices = [1, 7, 5, 3, 6, 4, 8, 2, 9]
        self.assertEqual(max_profit(prices), 20)

    def test11(self):
        prices = [10, 22, 5, 75, 65, 80]
        self.assertEqual(max_profit(prices), 97)
