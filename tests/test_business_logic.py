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

    def test_4(self):
        data = 'floordiv 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '1.0')

    def test_5(self):
        data = 'mod 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '3.0')

    def test_6(self):
        data = 'mul 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '28.0')

    def test_7(self):
        data = 'lt 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '0.0')

    def test_8(self):
        data = 'le 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '0.0')

    def test_9(self):
        data = 'eq 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '0.0')

    def test_10(self):
        data = 'ne 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '1.0')

    def test_11(self):
        data = 'ge 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '1.0')

    def test_12(self):
        data = 'gt 7 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '1.0')

    def test_13(self):
        data = 'pow 2 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '16.0')

    def test_14(self):
        data = 'truediv 2 4'
        result = logic.multi_func(data)
        self.assertEqual(result, '0.5')


if __name__ == '__main__':
    unittest.main()
