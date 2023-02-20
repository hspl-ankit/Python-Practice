'''Please write a program using a generator to print the even numbers between 0 and n in comma separated
form while n is input by the console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
In case of input data being supplied to the question, it should be assumed to be a console input
'''
def generetor(num):
    a= []
    for i in range(num):
        if i % 2 == 0:
            a.append(str(i)) 
    
    ans = ",".join(a)
    print(ans)
generetor(10)