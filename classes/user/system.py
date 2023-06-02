from classes.util import read_all_core_files

class User:
    '''Class to handle user information/meta data'''

    def __init__(self, name, age):
        '''
        Initialize the user's core functionality
        AIDEN will use this class to read information about the user and know how to communicate with them
        '''
        self.name = name if name else None
        self.age  = age if age else None
        
        # TODO: add more user commands
        self.user_commands = {
            0: "/name",
            1: "/remind",
            2: "/agree",
            3: "/remove",
            4: "/examine",
        }
        
        
    def userinfo(self):
        return [self.name, self.age]
    
    def check_user_command(self, command):
        '''check if the user command exists'''

        command = command.split(" ")[0]
        
        if command in self.user_commands.values():
            return True
        else:
            return False
    
    def handle_user_command(self, command):
        '''handles the validated user command'''
        for key, value in self.user_commands.items():
            if value == command:
                if key == 0:
                    return self._name()
                elif key == 1:
                    return self._remind()
                elif key == 2:
                    return self._agree()
                elif key == 3:
                    return self._remove()
                elif key == 4:
                    file_name = command.split(" ")[-1]
                    return self._examine(file_name)
                else:
                    return False
            else:
                continue
            
    def _name(self):
        '''ask the user for their name'''
        pass
    
    def _remind(self):
        '''remind AIDEN of the first message it received'''
        pass
    
    def _agree(self):
        '''make AIDEN restate all parameters and custom chat functions in organized list format'''
        pass
    
    def _remove(self):
        '''remove a file by file name'''
        pass
    
    def _examine(self, file_name):
        '''examine all data from python files within the docker container'''
        file_name = file_name.split(" ")[-1]
        print(file_name)
        return read_all_core_files(file_name)
    
    
    
    
