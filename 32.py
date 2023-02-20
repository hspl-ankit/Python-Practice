'''Define a function that can accept an integer number as input and print "It is an even number" if the number is
even, otherwise print "It is an odd number"'''

def check_odd_even(num):
    if num % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
num = int(input("Enter number: "))
check_odd_even(num)

