'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''

a = int(input("Enter number: "))
first = a * 11
second = a * 111
third = a * 1111
print(a+first+second+third)
