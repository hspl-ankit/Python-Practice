'''Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
Use random.sample() to generate a list of random values.
'''
import random

even_numbers = [num for num in random.sample(range(100, 201, 2), 5)]

print(even_numbers)
