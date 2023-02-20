'''Write a program which can filter even numbers in a list by using the filter function. The list is:
[1,2,3,4,5,6,7,8,9,10].
'''

lst = [1,2,3,4,5,6,7,8,9,10]
filtered = filter(lambda x: x%2 == 0, lst) 
print(list(filtered))