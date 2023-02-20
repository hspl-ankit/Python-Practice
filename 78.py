'''Please generate a random float where the value is between 10 and 100 using the Python math module.
Use random.random() to generate a random float in [0,1].
'''

import random
random_float = random.random()
scaled_float = random_float * 90 + 10

print(scaled_float)
