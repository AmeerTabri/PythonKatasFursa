import unittest
from katas.longest_common_prefix import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test1(self):
        list1 = ["flower", "flow", "flight"]
        list2 = ["dog", "racecar", "car"]
        list3 = []
        list4 = ["apple", "apricot", ""]
        list5 = ["eBay", "ebay"]

        self.assertEqual(longest_common_prefix(list1), "fl")
        self.assertEqual(longest_common_prefix(list2), "")
        self.assertEqual(longest_common_prefix(list3), "")
        self.assertEqual(longest_common_prefix(list4), "")
        self.assertEqual(longest_common_prefix(list5), "e")
