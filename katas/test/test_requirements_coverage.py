import unittest
from katas.requirements_coverage import select_minimal_test_cases


class TestSelectMinimalTestCases(unittest.TestCase):
    def test1(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertIn(set(result), [{2, 3}])

    def test2(self):
        test_cases = [
            [1, 2, 3, 4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0])

    def test3(self):
        test_cases = [
            [1],
            [2],
            [3],
            [4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set(result), {0, 1, 2, 3})

    def test4(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertTrue(set(result) in [{0, 1}, {0, 2}, {1, 2}])

    def test5(self):
        test_cases = [
            [1, 2],
            [2],
            [1]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set(result), {0})


if __name__ == "__main__":
    unittest.main()
