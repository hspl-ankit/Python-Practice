'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
Hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
str = input()
alpha = 0
digit = 0
for i in str:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    else:
        pass
print("LETTERS ",alpha,"\nDIGITS",digit)