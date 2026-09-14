import unittest
from utils import utils


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.u = utils()

    def test_reversed_integer(self):
        self.assertEqual(self.u.reversed(1234), 4321)
        self.assertEqual(self.u.reversed(10000), 1)
        self.assertEqual(self.u.reversed(-456), -654)
        self.assertEqual(self.u.reversed(0), 0)

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            self.u.reversed("123")
        with self.assertRaises(TypeError):
            self.u.reversed("hello")

    def test_reversed_float(self):
        with self.assertRaises((TypeError, ValueError)):
            self.u.reversed(123.45)
        with self.assertRaises((TypeError, ValueError)):
            self.u.reversed(12.0)

    def test_formatter_integer(self):
        self.assertEqual(self.u.formatter(10), ("0b1010", "0o12"))
        self.assertEqual(self.u.formatter(8), ("0b1000", "0o10"))
        self.assertEqual(self.u.formatter(0), ("0b0", "0o0"))

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            self.u.formatter("10")
        with self.assertRaises(TypeError):
            self.u.formatter("hello")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            self.u.formatter(10.5)
        with self.assertRaises(TypeError):
            self.u.formatter(8.0)


if __name__ == "__main__":
    unittest.main()
