import unittest
from katas.list_flatten import flatten_list


class TestlistFlatten(unittest.TestCase):
    nested_list1 = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]
    nested_list2 = [1,2,3]
    nested_list3 = []
    nested_list4 = [
        [[[1,2]]],
        [[[[[[[3]]]]]]],
        [[[[[4]],[5]],6]],
        [7, 8],
        [9, [10, [11]]],
        12
    ]
    def test1(self):
        self.assertEqual(flatten_list(self.nested_list1), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(flatten_list(self.nested_list2), [1,2,3])
        self.assertEqual(flatten_list(self.nested_list3), [])
        self.assertEqual(flatten_list(self.nested_list4), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
