import unittest
from katas.max_storage_capacity import max_storage_area


class TestMaxStorageCapacity(unittest.TestCase):
    def test1(self):
        containers = [2, 1, 5, 6, 2, 3]
        self.assertEqual(max_storage_area(containers), 10)

    def test2(self):
        containers = [1, 1]
        self.assertEqual(max_storage_area(containers), 1)

    def test3(self):
        containers = [4, 3, 2, 1, 4]
        self.assertEqual(max_storage_area(containers), 16)

    def test4(self):
        containers = [1, 2, 1]
        self.assertEqual(max_storage_area(containers), 2)

    def test5(self):
        containers = [1, 3, 2, 5, 25, 24, 5]
        self.assertEqual(max_storage_area(containers), 24)

    def test6(self):
        containers = []
        self.assertEqual(max_storage_area(containers), 0)

    def test7(self):
        containers = [10]
        self.assertEqual(max_storage_area(containers), 0)

    def test8(self):
        containers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        self.assertEqual(max_storage_area(containers), 12)
