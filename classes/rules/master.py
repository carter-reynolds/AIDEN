from classes.rules.rule_list import _rules

class AIDENRules:
    '''A class defining AIDEN's rules'''

    def __init__(self, _user:list):
        self.role = "AIDEN"
        self.rules = self._load_rules()

    def _load_rules(self):
        '''Load all rules'''
        rules = []

        for rule in _rules:
            rules.append(rule['rule_text'])

        return rules

    def get_rules(self):
        '''Return all rules'''
        return self.rules
