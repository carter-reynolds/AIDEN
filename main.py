import sys
import os

from classes.aiden.system import AIDENCore
from classes.rules.master import AIDENRules
from classes.user.system import User
                
def main(input_type):
    
    name = input("Name: ")

    while True:
        try:
            age = input("Age: ")
            age = int(age)
            break
        except:
            continue
        
    
    user  = User(name, age)
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
            response = aiden.communicate('user', command)
            continue
        

       

    
            


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please specify an input type: 'voice' or 'text'.")