'''With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all
duplicate values with the original order reserved.
Use set() to store a number of values without duplicates.
'''

original_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
new_list = []

for item in original_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)
