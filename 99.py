'''Define a class Person and its two child classes: Male and Female. All classes have a method called
"getGender" which can print "Male" for Male class and "Female" for the Female class.
Use Subclass(Parentclass) to define a child class'''

class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"
