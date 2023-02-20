'''Please write a program to output a random even number between 0 and 10 inclusive using a random module
and list comprehension.
Use random.choice() to a random element from a list.
'''
import random

even_nums = [num for num in range(0, 11) if num % 2 == 0]
random_even = random.choice(even_nums)

print(random_even)
