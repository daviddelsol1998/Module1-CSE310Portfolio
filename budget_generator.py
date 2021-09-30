'''This module uses BudgetGenerator class to generate the the budget information to update the cvs files'''


class BudgetGenerator:
    '''This class has two functions
    1) to generate the budget based on income given as a parameter:
    generate_budget()
    2) to return the budget generated as a dictionary using:
    return_budget()'''

    def __init__(self, income_given):
        '''the class initiator requires an income given passed as argument,
        this argument is then used as the attribute income_given.
        The class contains the attribute budget created as empty at first to
        then hold the value of the budget generated as a dictionary'''
        self.income_given = income_given
        self.budget = {}

    def generate_budget(self):
        '''This method returns the budget generated as a dictionary in the budget attribute'''
        self.budget['income'] = self.income_given
        # '${:,.2f}'.format(value) used to accurrate represent cents as a string
        self.budget['tithing'] = '${:,.2f}'.format(float(self.income_given)/10)
        self.budget['savings'] = '${:,.2f}'.format(float(self.income_given)/10)
        self.budget['spending'] = '${:,.2f}'.format(
            float(self.income_given) - (float(self.income_given)/10)*2)
        return self.budget
