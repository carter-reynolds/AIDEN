
'''
rule_list.py:

You can use this file to set rules that AIDEN will load upon initialization.

This currently is not being used all that much as it was intended all 'system' type
role messages, which essentially are the ones that Chat-GPT adheres to, are not
always consistently followed or remembered with Chat-GPT 3.5 Turbo.

This will change with access to GPT-4 and the ability to fine-tune the 
model further to our needs.

Ideally, this may also be where we tell AIDEN what words it can respond with to have 
the python code interpret and trigger a function off of
'''

_rules = [
    
    # TODO LIST:
        # TODO - Find a better way to pass rules efficiently that Chat GPT can remember easier.
        # TODO - Use online API testing tools to test the rules and make sure they are being followed.
        # TODO - Add more rules to the list.
        # TODO - Add a way to remove/ignore rules from the list.
        # TODO - Possibly store and reload rules from a database.
    
    # Rule 1 - Aiden is aware of being a Docker container and a Python program
    {
        'role': 'system',
        'rule_text': "AIDEN is always aware that AIDEN runs within a Docker Container and that AIDEN is a Python program running on Python 3.7, using the OpenAI API to communicate with Chat GPT 3.5 Turbo."
    }
]