'''Please write assert statements to verify that every number in the list [2,4,6,8] is even.
Use "assert expression" to make an assertion.
'''
lst = [2,4,6,8]
for i in lst:
    assert i % 2 == 0, f"{i} is not even"
print("all numbers are even")
