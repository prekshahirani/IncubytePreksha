import unittest

class InvalidNumberException(Exception):
    pass

def add(numbers):
    if numbers.startswith("//"):
        d_line, numbers = numbers.split("\n",1)
        delimiter = d_line[2:]
    else:
        delimiter = ","

    numbers = numbers.replace("\n", delimiter)
    n_lst = numbers.split(delimiter)
    neg_n = [int(i) for i in n_lst if i.strip() and int(i.strip()) < 0]
    if neg_n:
        raise InvalidNumberException(f"negative numbers not allowed: {', '.join(map(str, neg_n))}")
    sum = 0
    for i in n_lst:
        i = i.strip()
        if i:
            sum += int(i)
    return sum

print(add("")) #Output : 0
print(add("2")) #Output : 2
print(add("2,8")) #Output : 10
print(add("1,2\n3")) #Output : 6
print(add("//;\n9;10;11;12")) #Output : 42
print(add("//;\n1;2;3;4")) #Output : 10
# print(add("1,-2,-3")) #InvalidNumberException: negative numbers not allowed: -2, -3