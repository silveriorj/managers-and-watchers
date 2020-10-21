import json
import unittest


filename = 'data/source_file.json'
m_file = 'managers.json'
w_file = 'watchers.json'


class Tests(unittest.TestCase):

    def test_source_file(self):
        with open(filename) as json_file:
            data = json.load(json_file)
        self.assertEqual(isinstance(data, list), True, "Should be List")

    def test_managers_file(self):
        with open(m_file) as json_file:
            data = json.load(json_file)
        self.assertEqual(isinstance(data, dict), True, "Should be Dict")

    def test_watchers_file(self):
        with open(w_file) as json_file:
            data = json.load(json_file)
        self.assertEqual(isinstance(data, dict), True, "Should be Dict")


if __name__ == '__main__':
    unittest.main()
