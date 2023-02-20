'''Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input.
We can define a recursive function in Python.
'''

def cal(num):
    a = 0 
    if num>0:
            a = cal(num-1) + 100
    return a
a = int(input("Enter Number: "))
print(cal(a))
