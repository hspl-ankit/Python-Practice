'''Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit
of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
even_digits_numbers = []

for i in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(i)):
        even_digits_numbers.append(str(i))

print(",".join(even_digits_numbers))

