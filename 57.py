'''Please write a program which prints all permutations of [1,2,3]
Use itertools.permutations() to get permutations of lists
'''
import itertools

lst = [1,2,3]
permutation  = itertools.permutations(lst)
print(list(permutation))