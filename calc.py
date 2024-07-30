import unittest

def add(numbers):
    if not numbers:
        return 0
    return int(numbers)

class TestCalc(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(add(""),0)
    def test_single_input(self):
        self.assertEqual(add(""), 1)

if __name__ == '__main__':
    add(2)
    unittest.main()