'''Define a function which can generate and print a list where the values are square of numbers between 1 and
20 (both included).'''
def pritn_list():
    lst = []
    for i in range(1,21):
        lst.append(i**2)
    print(lst)
pritn_list()