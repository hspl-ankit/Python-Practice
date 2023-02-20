''''Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1
and 1000 inclusive.
Use random.sample() to generate a list of random values.'''

import random

divisible_by_5_and_7 = [n for n in range(1, 1001) if n % 5 == 0 and n % 7 == 0]
random_numbers = random.sample(divisible_by_5_and_7, 5)

print(random_numbers)
