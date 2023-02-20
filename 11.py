'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then
check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma
separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
In case of input data being supplied to the question, it should be assumed to be a console input'''

digit  =  [x for x in input().split(",")]
ans1 = []
for i in range(len(digit)):
    if len(digit[i]) == 4:
        if (digit[i][0]) !='0':
            if int(digit[i]) % 5 == 0:
                ans1.append(digit[i])
    else:
        print("Enter valid numner ")
ans  = ",".join(ans1)
print(ans)

