'''Question 17 Level 2
Write a program that computes the net amount of a bank account based on a transaction log from console
input. The transaction log format is shown as follows:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

a = []
deposite = []
withdraw = []
while True:
    line = input()
    if line:
        a.append(line)
    else:
        break
    digit = line.split()

    for i in range(len(digit)):
        if digit[i] == 'D':
            deposite.append(digit[i+1])
        if digit[i] == 'W':
            withdraw.append(digit[i+1])

depo = 0
wido = 0
for a in deposite:
    depo += int(a)
for b in withdraw:
    wido += int(b)
print(depo-wido)


