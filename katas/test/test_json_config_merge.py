import unittest
import json
import os
from katas.json_config_merge import json_configs_merge


def write_json_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


class TestIsUniqueStr(unittest.TestCase):

    def tearDown(self):
        # Remove all test JSON files after each test
        for filename in [
            'test1.json', 'test2.json', 'test3.json',
            'test4.json', 'test5.json', 'test6.json'
        ]:
            if os.path.exists(filename):
                os.remove(filename)

    def test1(self):
        # Single file
        write_json_file('test1.json', {"a": 1, "b": 2})
        result = json_configs_merge('test1.json')
        self.assertEqual(result, {"a": 1, "b": 2})

    def test2(self):
        # Two files, no conflict
        write_json_file('test1.json', {"a": 1})
        write_json_file('test2.json', {"b": 2})
        result = json_configs_merge('test1.json', 'test2.json')
        self.assertEqual(result, {"a": 1, "b": 2})

    def test3(self):
        # Two files, with override
        write_json_file('test1.json', {"a": 1, "b": 2})
        write_json_file('test2.json', {"b": 3})
        result = json_configs_merge('test1.json', 'test2.json')
        self.assertEqual(result, {"a": 1, "b": 3})

    def test4(self):
        # Nested override
        write_json_file('test1.json', {"user": {"name": "Alice", "age": 25}})
        write_json_file('test2.json', {"user": {"age": 26}})
        result = json_configs_merge('test1.json', 'test2.json')
        self.assertEqual(result, {"user": {"name": "Alice", "age": 26}})

    def test5(self):
        # Deep nested override
        write_json_file('test1.json', {"cfg": {"ui": {"theme": "light", "lang": "en"}}})
        write_json_file('test2.json', {"cfg": {"ui": {"lang": "es"}}})
        result = json_configs_merge('test1.json', 'test2.json')
        self.assertEqual(result, {"cfg": {"ui": {"theme": "light", "lang": "es"}}})

    def test6(self):
        # Multiple levels, multiple merges
        write_json_file('test1.json', {"x": 1, "y": {"a": 1}})
        write_json_file('test2.json', {"y": {"b": 2}})
        write_json_file('test3.json', {"z": 3})
        result = json_configs_merge('test1.json', 'test2.json', 'test3.json')
        self.assertEqual(result, {"x": 1, "y": {"a": 1, "b": 2}, "z": 3})


if __name__ == '__main__':
    unittest.main()
