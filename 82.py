'''Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
Use random.sample() to generate a list of random values.
'''
import random

random_numbers = random.sample(range(100, 201), 5)
print(random_numbers)
