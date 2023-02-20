'''Please write a program to print the running time of execution of "1+1" for 100 times.
Use timeit() function to measure the running time.
'''

import timeit
t = timeit.timeit(stmt='1+1', number=100)
print('Execution time:', t, 'seconds')

