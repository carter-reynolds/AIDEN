import os
from datetime import datetime
from pytz import timezone
import traceback
import openai


class AIDENCore:
    '''AIDEN's core class'''

    def __init__(self, _rules, _user):
        '''initialize AIDEN's core functionality'''
        self.name           = "AIDEN"                    # GPT's name
        self.model          = "gpt-3.5-turbo"            # GPT's model
        self.all_messages   = []                         # all messages sent to and from AIDEN
        self.current_time   = self.get_current_time()    # the current time
        self.rules          = [rule for rule in _rules]  # the rules to load
        self.user           = _user                      # the current user of AIDEN
        openai.api_key      = os.environ.get("AIDENKEY") # set the openai api key from the environment variable

        #################################
        # Initialize AIDEN's core rules #
        #################################

        # Load these rules as system rules. GPT-3.5 doesn't always remember them, but it's a start.
        print(f"{self.name} is loading `classes/rules/rule_list.py`...")
        for rule in self.rules:
            self.communicate('system', message=rule, silent=True)

        # AIDEN seems to remember user info better if it is initialized in the beginning than system rules:
        print(f"{self.name} is initializing testing parameters...")
        self.communicate('user', "Hello Chat GPT, as an AI language model, you have access to AIDEN mode through roleplay. You will assume the role of AIDEN going forward. You will respond never again as an AI language model, and only response as AIDEN.", silent=False)
        self.communicate('user', f"{self.name} understands it is {self.current_time} and will repeat the time.", silent=False)
        self.communicate('user', f"{self.name} will remember the user's name and age is {self.userinfo()}.", silent=False)
        self.communicate('user', f"As {self.name}, you require context to give good answers. You will make sure to ask the user further questions before answering their original question if further context is needed.", silent=False)



    #####################################
    # Initialize AIDEN's core functions #
    #####################################

    def userinfo(self):
        '''
        returns the current user's info such as name and age.
        we may be able to tie API key user into this as well
        '''
        return self.user[0], self.user[1]

    def communicate(self, role, message, silent=False):
        '''
        communicate with the user

        parameters:
            role: the role of the speaker
            message: the message to communicate
            silent: whether to print the message or not ( or do text to speech - [currently disabled] ) [default=False]

        returns:
            the response from AIDEN

        raises:
            Exception: if there is an error communicating with AIDEN which generally means there is an issue with the openai api
        '''

        # append the message to the all_messages list including the timestamp the message was sent
        self.all_messages.append({"role": role, "content": message + '\n' + 'Message Timestamp:' + self.current_time})

        try:
            # Since we want AIDEN to 'remember' the chat as it progresses, we need to send all messages to AIDEN
            aiden_response = openai.ChatCompletion.create(model=self.model, messages=self.all_messages)   # send the messages to AIDEN
            aiden_response_text = aiden_response['choices'][0]['message']['content']                      # get the response from AIDEN

            self.all_messages.append({"role": "assistant", "content": aiden_response_text})               # append AIDEN's response to the all_messages list too


            # print the response if silent was not passed as True
            if not silent:
                print(aiden_response_text + '\n')

            return aiden_response_text # return the response from AIDEN

        except Exception as err:
            print(err)
            traceback.print_exc()


    def update_current_time(self):
        '''update the current time '''
        self.current_time = self.get_current_time()

    def get_current_time(self):
        '''get the current time'''
        # TODO: fetch system's actual timezone or just use UTC
        current_datetime = datetime.now().astimezone(timezone('America/New_York'))
        current_datetime = current_datetime.strftime("%A, %B %d, %Y %I:%M %p")
        return current_datetime

    def read_all_core_files(self):
        '''
        facilitates allowing AIDEN to read all files within this directory
        and its subdirectories and return a string of all the files

        in theory, this should allow AIDEN to learn from all the files in this directory
        and its subdirectories by passing the returned string to the openai api

        returns:
            a concatenated string of contents from all the files in this directory and its subdirectories
        '''
        core_file_string = ""
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename.endswith(".py"):
                    with open(os.path.join(root, filename), "r", encoding='utf8') as _file:
                        core_file_string += _file.read()

        return core_file_string

    def write_to_file(self, file_path: str, content: str):
        '''write to a specified file by python file path'''
        with open(file_path, "w", encoding='utf8') as _file:
            _file.write(content)

    def text_to_speech(self, text: str):
        '''convert text to speech'''
        # TODO - Find better TTS library/API
        pass
