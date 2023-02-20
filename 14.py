'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case
letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

upper = 0
lower = 0
str = input("Enter input: ")
for i in str:
    if i.isupper():
        upper += 1
    elif i.lower():
        lower += 1
print("UPPER CASE",upper,"\nLOWER CASE",lower)