'''Write a program which can filter() to make a list whose elements are an even number between 1 and 20 (both
included).
'''
result = list(filter(lambda x : x%2 == 0,range(1,21)))
print(result)