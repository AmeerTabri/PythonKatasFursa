import unittest
from katas.do_n_times import say_hello


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(say_hello(), "Hello!")
