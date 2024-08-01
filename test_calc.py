import unittest
from calc import add, InvalidNumberException

class TestCalc(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(add(""),0)
    def test_single_input(self):
        self.assertEqual(add("1"), 1)
    def test_two_input(self):
        self.assertEqual(add("1,2"), 3)
    def test_multiple_input(self):
        self.assertEqual(add("1,2,3,4"), 10)
    def test_new_lines(self):
        self.assertEqual(add("1\n2,3\n4"), 10)
    def test_diff_delimiters(self):
        self.assertEqual(add("//;\n1;2;3;4"), 10)
    def test_negative_input(self):
        with self.assertRaises(InvalidNumberException) as cm:
            add("1,-2,3")
        self.assertEqual(str(cm.exception), "negative numbers not allowed: -2")
    def test_all_positive_numbers(self):
        self.assertEqual(add("1,2,3,4"), 10)
        self.assertEqual(add("5\n6,7\n8"), 26)
        self.assertEqual(add("//;\n9;10;11;12"), 42)
if __name__ == '__main__':
    unittest.main()