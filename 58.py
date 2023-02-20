'''Write a function to compute 5/0 and use try/except to catch the exceptions.
Use try/except to catch exceptions.'''

try:
    print(5/0)
except ZeroDivisionError as e :
    print("Error: ",e)