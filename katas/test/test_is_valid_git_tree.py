import unittest
from katas.is_valid_git_tree import is_valid_git_tree


class TestWordCount(unittest.TestCase):
    def test1(self):
        tree1 = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        self.assertTrue(is_valid_git_tree(tree1))

        tree2 = {
            "A": ["B"],
            "C": ["D"],
            "B": [],
            "D": []
        }
        self.assertFalse(is_valid_git_tree(tree2))

        tree3 = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]
        }
        self.assertFalse(is_valid_git_tree(tree3))

        tree4 = {
            "A": ["B"],
            "B": [],
            "C": ["D"],
            "D": [],
            "E": []
        }
        self.assertFalse(is_valid_git_tree(tree4))

        tree5 = {
            "A": []
        }
        self.assertTrue(is_valid_git_tree(tree5))

        tree6 = {
                "A": ["B", "C", "D"],
                "B": ["E", "F"],
                "C": ["G", "H"],
                "D": ["I", "J"],
                "E": ["K", "L"],
                "F": ["M"],
                "G": [],
                "H": ["N", "O"],
                "I": [],
                "J": ["P"],
                "K": [],
                "L": [],
                "M": [],
                "N": [],
                "O": [],
                "P": ["Q", "R"],
                "Q": [],
                "R": []
        }
        self.assertTrue(is_valid_git_tree(tree6))
