'''Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included)
and the values are square of keys.
'''

def Print_dict():
    dic = {}
    for i in range(1,4):
        dic[i] = i**2
    print(dic) 
Print_dict()