# String Calculator TDD Kata

- This project implements a simple ***String Calculator*** according to Test-Driven Development(TDD) approach.
- The add method takes a string of comma-separated numbers (with support for different delimiters and new lines) and returns the sum of those numbers.
- Throws an exception with a message listing all negative numbers when any negative numbers are given.
- Supports zero and single digit inputs.

## Clone the repository
   
   https://github.com/prekshahirani/IncubytePreksha.git

## Handling different input formats

1. **Empty String :** Returns 0.

2. **Single Digit :** Returns number.

3. **Multiple Inputs :** Returns sum of the numbers.

4. **New Line As Delimeter :** Returns sum of all the numbers.

5. **Multiple Delimeters :** Handles many delimeters.

6. **Negative Numbers :** Throws execption and list all the negative numbers.

- Inputs are given in comma-seperated manner.

## Code Format

- **Add Function :** add(str)

- **print(add(""))** #Output : 0

- **print(add("2"))** #Output : 2

- **print(add("2,8"))** #Output : 10

- **print(add("1,2\n3"))** #Output : 6

- **print(add("//;\n9;10;11;12"))** #Output : 42

- **print(add("//;\n1;2;3;4"))** #Output : 10

- **print(add("1,-2,-3"))** #InvalidNumberException: negative numbers not allowed: -2, -3

