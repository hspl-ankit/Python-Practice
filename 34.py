'''Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys.'''

def print_dict():
    dic = {}
    for i in range(1,21):
        dic[i] =  i**2
    print(dic)
print_dict()