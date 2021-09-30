'''This module uses BudgetGenerator class to generate the the budget information to update the cvs files'''

class BudgetGenerator:
    '''This class has two functions
    1) to generate the budget based on income given as a parameter:
    generate_budget()
    2) to return the budget generated as a dictionary using:
    return_budget()'''
    
    def __init__(self,income_given):
        self.budget = {}
