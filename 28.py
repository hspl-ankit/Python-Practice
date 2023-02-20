'''Define a function that can convert an integer into a string and print it in console.
Use str() to convert a number to string.
'''
def conv_int_string(string):
    string = str(string)
    print(f"the type of your input is {type(string)} and your input is {string}")

intp = int(input("Enter int Value: "))
conv_int_string(intp)