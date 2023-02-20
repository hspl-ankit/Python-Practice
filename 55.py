'''Define a class named Shape and its subclass Square. The Square class has an init function which takes a
length as an argument. Both classes have an area function which can print the area of the shape where the
Shape's area is 0 by default.'''

class Shape:
    def __init__(self,length):
        self.lenght = length

    def area(self):
            return 0

class Squre(Shape):
    def area(self):
        return self.lenght ** 2

squre = Squre(5)
print(squre.area())