import unittest
from unittest.mock import MagicMock
from katas.do_n_times import do_n_times, say_hello, print_message


class TestDoNTimes(unittest.TestCase):
    def test1(self):
        self.assertEqual(say_hello(), say_hello())