import unittest
from katas.semantic_version_comparator import compare_versions


class TestCompareVersions(unittest.TestCase):
    def test1(self):
        self.assertEqual(compare_versions("1.0.0", "1.0.0"), 0)
        self.assertEqual(compare_versions("1.2", "1.2.0"), 0)
        self.assertEqual(compare_versions("0.0.0", "0.0.0"), 0)

    def test2(self):
        self.assertEqual(compare_versions("2.0.0", "1.9.9"), 1)
        self.assertEqual(compare_versions("1.10.0", "1.2.0"), 1)
        self.assertEqual(compare_versions("1.0.1", "1.0.0"), 1)

    def test3(self):
        self.assertEqual(compare_versions("1.0.0", "1.0.1"), -1)
        self.assertEqual(compare_versions("0.9.9", "1.0.0"), -1)
        self.assertEqual(compare_versions("1.2.3", "1.2.4"), -1)

    def test4(self):
        self.assertEqual(compare_versions("1", "1.0.0.0"), 0)
        self.assertEqual(compare_versions("1.0.1", "1"), 1)
        self.assertEqual(compare_versions("1.0.0", "1.0.1.0.0.0"), -1)

    def test5(self):
        self.assertEqual(compare_versions("01.002.0003", "1.2.3"), 0)
        self.assertEqual(compare_versions("1.02.0", "1.1.9"), 1)
        self.assertEqual(compare_versions("1.2.0", "1.02.0"), 0)

    def test6(self):
        self.assertEqual(compare_versions("10.0.0", "2.0.0"), 1)
        self.assertEqual(compare_versions("1.999.999", "2.0.0"), -1)

    def test7(self):
        # Complex version with many levels and leading zeros
        self.assertEqual(compare_versions("1.0.0.0.0.1", "1.0.0"), 1)
        self.assertEqual(compare_versions("1.0.0.0.0.0", "1.0"), 0)
        self.assertEqual(compare_versions("1.0.0.0.1", "1.0.0.1"), -1)
        self.assertEqual(compare_versions("1.0.0.0.1", "1.0.0.0.0.2"), 1)


if __name__ == '__main__':
    unittest.main()
