import unittest
from katas.word_count import count_words


class TestWordCount(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("     "), 0)
        self.assertEqual(count_words("   Hello World   "), 2)
        self.assertEqual(count_words("word1  word2   word3"), 3)
        self.assertEqual(count_words("Hello"), 1)
        self.assertEqual(count_words("Hello\nworld\tHello\nworld\t"), 4)
        self.assertEqual(count_words("Wait... what?! no way!"), 4)
