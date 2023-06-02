import os
import sys

def read_all_core_files(file_name):
    '''
    facilitates allowing AIDEN to read all files within this directory
    and its subdirectories and return a string of all the python files

    in theory, this should allow AIDEN to learn from all the files in this directory
    and its subdirectories by passing the returned string to the openai api

    returns:
        a list of all the python files in this directory and its subdirectories
    '''

    _af = {}
    
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(".py") and filename == file_name:
                # Add the filename to _af
                _af[filename] = {}
                print(_af)
                with open(os.path.join(root, filename), "r") as _file:
                    _af[filename]['content'] = _file.read()
                    _af[filename]['path'] = os.path.join(root, filename)
                    _af[filename]['size'] = os.path.getsize(os.path.join(root, filename))
                    _af[filename]['last_modified'] = os.path.getmtime(os.path.join(root, filename))
                    _af[filename]['created'] = os.path.getctime(os.path.join(root, filename))
    return _af

def write_to_file(self, file_path: str, content: str):
    '''write to a specified file by python file path'''
    with open(file_path, "w", encoding='utf8') as _file:
        _file.write(content)
