

class User:
    
    def __init__(self, name, age):
        '''
        Initialize the user's core functionality
        
        AIDEN will use this class to read information about the user and know how to communicate with them
        '''
        self.name = name
        self.age  = age
        
    def userinfo(self):
        return [self.name, self.age]

        
        