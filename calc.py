import unittest

def add(numbers):
    if not numbers:
        return 0
    numbers = numbers.replace("\n",",")
    num_lst = numbers.split(",")
    sum = 0
    for i in num_lst:
        sum += int(i)
    return sum

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
if __name__ == '__main__':
    unittest.main()