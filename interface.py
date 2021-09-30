'''This module handles the user interface and all the information to be displayed
to the user, it relies on the date and os modules for some of its functionality.'''
from datetime import date  # library used to get current date
import os  # library used to clear screen at printing


class UserInterface:
    '''This class handles 5 methods.
    1) get_user(): recieves user name as input string and return it
    to be used for file handling.
    2) get_amount(): recives amount to be used for budget creation in float format
    3) get_date(): receives date in string format,
    this date will be used to retrieve previous budget
    4) display_budget_header(): displays current date and budget of given date
    5) select_options() : ask user what to do and return users selection as a string'''

    def __init__(self):
        '''initializes the ui class, clears screen using os module.
        Gets the current date from datetime module 
        and welcomes user displaying current date'''
        os.system('cls' if os.name == 'nt' else 'clear') # this clears the console
        self.current_date = date.today()
        print(f'Todays date: {self.current_date}')
        print('Welcome to the budget manager' + '\n')

    def get_user(self):
        '''recieves user name as input string and return it
        to be used for file handling'''
        self.user_name = input('What is your name: ')
        return self.user_name

    def get_amount(self):
        '''recives amount to be used for budget creation in float format'''
        print('ONLY USE "." FOR CENTS IF NEEDED, DO NOT USE ","')
        self.new_amount = float(input('Please input the amount here: $'))
        return self.new_amount

    def get_date(self):
        '''receives date in string format,
        this date will be used to retrieve previous budget'''
        print('USE THE FOLLOWING DATE FORMAT MM/DD/YYYY')
        self.new_date = input(
            'Please input the date of your reported income to see budget: ')
        return self.new_date

    def display_budget_header(self, new_date):
        '''displays current date and budget of given date'''
        print(f'Current date: {self.current_date}')
        print(f'Budget of income received on: {new_date}')

    def select_options(self):
        '''ask user what to do and return users selection as a string'''
        print('Press "P" to see a previous budget given based on the income date')
        print('Press "B" to create a budget based on new income')
        self.user_selection = input('What would you like to do?: ')
        return self.user_selection
