'''Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
Use list comprehension to delete a bunch of elements from a list.
'''

lst = [5, 6, 77, 45, 22, 12, 24]

lst = [x for x in lst if x % 2 != 0]

print(lst)
