import unittest
from katas.time_me import measure_execution_time, time

class TestTimeMe(unittest.TestCase):
    def test_hello_world(self):
        def hello_world():
            return "Hello, world!"

        # Should be very fast, but still measurable (> 0 ms)
        duration = measure_execution_time(hello_world)
        self.assertGreaterEqual(duration, 0)
        self.assertLess(duration, 3)

    def test_sleep_function(self):
        def slow_function():
            time.sleep(5)  # 200ms

        duration = measure_execution_time(slow_function)
        self.assertGreaterEqual(duration, 5000)
        self.assertLess(duration, 5010)

    def test_instant_function(self):
        def instant():
            pass

        duration = measure_execution_time(instant)
        self.assertGreaterEqual(duration, 0)
        self.assertLess(duration, 1)
