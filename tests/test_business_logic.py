import unittest
import math_server.package.mathematical_logic as logic


class TestLogic(unittest.TestCase):
    def test_1(self):
        data = 'add 3 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '7.0')

    def test_2(self):
        data = 'sub 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '3.0')

    def test_3(self):
        data = 'dfg 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
