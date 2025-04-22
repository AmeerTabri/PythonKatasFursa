import unittest
from katas.is_unique_str import is_unique


class TestIsUniqueStr(unittest.TestCase):
    def test(self):
        self.assertEqual(is_unique("Hello"), False)
        self.assertEqual(is_unique("Ameer"), False)
        self.assertEqual(is_unique("Amir"), True)
        self.assertEqual(is_unique("Aa"), True)
        self.assertEqual(is_unique(""), True)
        self.assertEqual(is_unique("a1234"), True)
        self.assertEqual(is_unique("!@$##"), False)
        self.assertEqual(is_unique('Abc!@$#"123'), True)
