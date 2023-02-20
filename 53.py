'''Define a class named Circle which can be constructed by a radius. The Circle class has a method which can
compute the area.
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius ** 2)
        
Circle1 = Circle(5)
print(Circle1.area())
