'''Write a program which can map() to make a list whose elements are squares of numbers between 1 and 20
(both included)'''

result = list(map(lambda x : x*x, range(1,21)))
print(result)