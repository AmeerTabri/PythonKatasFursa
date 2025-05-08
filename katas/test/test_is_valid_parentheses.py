import unittest
from katas.is_valid_parentheses import is_valid_parentheses


class TestisValidParentheses(unittest.TestCase):
    def test1(self):
        # Valid cases
        self.assertTrue(is_valid_parentheses("()[]{}"))
        self.assertTrue(is_valid_parentheses("{[]()}"))
        self.assertTrue(is_valid_parentheses("(([]){})"))
        self.assertTrue(is_valid_parentheses("(([]){})()()[][]"))
        self.assertTrue(is_valid_parentheses("([{([{}])}])"))
        self.assertTrue(is_valid_parentheses(""))

        # Invalid cases
        self.assertFalse(is_valid_parentheses("(]"))
        self.assertFalse(is_valid_parentheses("([)]"))
        self.assertFalse(is_valid_parentheses("("))
        self.assertFalse(is_valid_parentheses("]"))
        self.assertFalse(is_valid_parentheses("((("))
        self.assertFalse(is_valid_parentheses("(()"))
        self.assertFalse(is_valid_parentheses("([{([{(}])}])"))
