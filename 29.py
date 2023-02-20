'''Define a function that can receive two integral numbers in string form and compute their sum and then print it
in the console.
Use int() to convert a string to integer.'''

def cal_sum(num1,num2):
    num1 =  int(num1)
    num2 = int(num2)
    print(f"sum is {num1+num2}")
num1  = input("Enter number1: ")
num2 = input("Enter number 2: ")
cal_sum(num1,num2)
