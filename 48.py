'''Write a program which can map() and filter() to make a list whose elements are square or even numbers in
[1,2,3,4,5,6,7,8,9,10].
'''
lst = [1,2,3,4,5,6,7,8,9,10]
mape = map(lambda x : x*x,lst )
evensqure = filter(lambda x : x % 2 == 0, mape )
filttered = filter(lambda x: x%2 == 0,lst)
print(list(evensqure))
print(list(filttered))



