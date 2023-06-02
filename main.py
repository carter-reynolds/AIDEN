import sys
from classes.aiden.system import AIDENCore
from classes.rules.master import AIDENRules
from classes.user.system  import User

def main():

    # Collect user info and initialize AIDEN, USER, and RULE objects
    user        = User("", 0)
    uinfo       = user.userinfo()
    aiden_rules = AIDENRules().get_rules()
    aiden       = AIDENCore(aiden_rules, uinfo)

    while True:
        user_input = input("==> ")
        if user_input:
            
            print(user_input)
            
            command_check = user.check_user_command(user_input)
            
            if command_check is False:
                print("1")
                aiden.communicate('user', user_input)
            else:
                if user_input.startswith("/examine"):
                    print("2")
                    file_content = user.handle_user_command(user_input)
                    aiden.examine_file(file_content)

        continue
    



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "text":
            main()
        else:
            # Eventually will re-enable voice input. It worked by Voice to Text API was too slow.
            print("Please specify an input type: 'text'.")
    else:
        print("Please specify an input type: 'text'.")