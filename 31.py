'''Define a function that can accept two strings as input and print the string with maximum length in the console.
If two strings have the same length, then the function should print all strings line by line'''

def print_long_string(string1,string2):
    if len(string1)>len(string2):
        print(string1)
    elif len(string2)>len(string1):
        print(string2)
    else:
        print(string1)
        print(string2)

string1 = input("Enter Input 1: ")
string2 = input("Enter Input 2: ")
print_long_string(string1,string2)