
import pyttsx3
import sys

from classes.aiden.system import AIDENCore
from classes.rules.master import AIDENRules
from classes.user.system import User

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

                
def main(input_type):
    
    user  = User("Carter", 27)
    uinfo = user.userinfo()
    aiden_rules = AIDENRules(uinfo).get_rules()
    aiden = AIDENCore(aiden_rules, uinfo)
    
    while True:
        if input_type == "text":
            command = input("==> ")
        else:
            print("Invalid input type. Please use 'voice' or 'text'.")
            break

        if command:
            if aiden.communicate(command):
                pass
            else:
                print("AIDEN could not understand you for some reason.")
                break
        else:
            print("AIDEN could not understand you for some reason.")
            break

    
            


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please specify an input type: 'voice' or 'text'.")