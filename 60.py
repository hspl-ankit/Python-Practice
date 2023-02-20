'''Define a custom exception class which takes a string message as an attribute.
To define a custom exception, we need to define a class inherited from Exception.'''

class CustomException(Exception):
    def __init__(self, message):
        self.message = message      

raise CustomException("This is Custom exception")
 