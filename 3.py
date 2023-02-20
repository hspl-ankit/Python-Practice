'''Write a program which can compute the factorial of a given number.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def fect (num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num*fect(num-1)

num = int(input("Enter Number you want to find fectorial: "))
ans = fect(num)
print(ans)