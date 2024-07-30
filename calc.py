import unittest

def add(numbers):
    if numbers.startswith("//"):
        d_line, numbers = numbers.split("\n",1)
        delimiter = d_line[2:]
    else:
        delimiter = ","
    
    numbers = numbers.replace("\n", delimiter)
    n_lst = numbers.split(delimiter)
    sum = 0
    for i in n_lst:
        i = i.strip()
        if i:
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
    def test_diff_delimiters(self):
        self.assertEqual(add("//;\n1;2;3;4"), 10)
if __name__ == '__main__':
    unittest.main()