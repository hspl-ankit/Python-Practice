'''Write a method which can calculate square value of number'''

class number:
    def cal_squre(self, num):
        return num**2
num = int(input("Enter number you want to squre: "))
a = number()
print(f"Squre is {a.cal_squre(num)}")

