import sys
from classes.aiden.system import AIDENCore
from classes.rules.master import AIDENRules
from classes.user.system  import User

def main(input_type):

    name = input("Name: ")

    while True:
        try:
            age = input("Age: ")
            age = int(age)
            break
        except:
            continue

    # Collect user info and initialize AIDEN, USER, and RULE objects
    user        = User(name, age)
    uinfo       = user.userinfo()
    aiden_rules = AIDENRules(uinfo).get_rules()
    aiden       = AIDENCore(aiden_rules, uinfo)

    while True:
        
        # if launched with 'text' arg, create text prompt
        if input_type == "text":
            command = input("==> ") 
        else:
            print("Invalid input type. Please use 'voice' or 'text'.")
            break
        
        # send the user's input to AIDEN if command was not empty
        if command:
            response = aiden.communicate('user', command)
            continue


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        # Eventually will re-enable voice input. It worked by Voice to Text API was too slow.
        print("Please specify an input type: 'voice' or 'text'.")