import unittest

def add(numbers):
    return 0;

class TestCalc(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(add(""),0)

if __name__ == '__main__':
    unittest.main()