'''Define a function which can compute the sum of two numbers.
Define a function with two numbers as arguments. You can compute the sum in the function and return the
value.
'''
def cal_sum(num1, num2):
    return num1 + num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"sum is {cal_sum(num1,num2)}")
