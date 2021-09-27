'''This module handles the user interface and all the information to be displayed
to the user'''
from datetime import date


class UserInterface:
    '''This class handles two main functions, it greets the users,and it receives input
    which is used to allow users to retrive previous budgets or create a budget based on
    new income.'''

    def __init__(self):
        '''initializes the ui class
        gets the current date and welcomes user'''
        self.current_date = date.today()
        print(self.current_date)
        print('Welcome to the budget manager')

    def get_user(self):
        '''recieves user name as input to be used for file handling'''
        self.user_name = input('What is your name:')

    def input_amount(self):
        '''recives amount to be used for budget creation in float format'''
        self.new_amount = input('Please input the amount here: $')

    def input_date(self):
        '''receives date to retrive previous budget in string format'''
        print('USE THE FOLLOWING DATE FORMAT (MM/DD/YYYY)')
        self.new_date = input(
            'Please input the date of your reported income to see budget:')

    def display_budget_header(self):
        print(f'Todays date:{self.current_date}')
        print(f'Budget of income received on: {self.new_date}')
