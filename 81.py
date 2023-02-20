'''Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive
using a random module and list comprehension.
Use random.choice() to a random element from a list'''

import random

numbers = [num for num in range(0, 11) if num % 5 == 0 and num % 7 == 0]
random_number = random.choice(numbers)

print(random_number)