'''Write a program which can map() to make a list whose elements are square of elements in
[1,2,3,4,5,6,7,8,9,10].'''

lst = [1,2,3,4,5,6,7,8,9,10]
mape = map(lambda x: x * x  , lst)
print(list(mape))