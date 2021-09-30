'''This module handles the user interface and all the information to be displayed
to the user, it relies on the date and os modules for some of its functionality.'''
from datetime import date  # library used to get current date
import os  # library used to clear screen at printing


class UserInterface:
    '''This class handles 6 methods.
    1) get_user(): recieves user name as input string and return it
    to be used for file handling.
    2) get_amount(): recives amount to be used for budget creation in string format
    3) get_date(): receives date in string format,
    this date will be used to retrieve previous budget
    4) display_budget_header(): displays current date and budget of given date
    5) select_options() : ask user what to do and return users selection as a string
    6) clear(): clear screen'''

    def __init__(self):
        '''initializes the ui class and calls clear()
        to clear screen.
        Gets the current date from datetime module 
        and welcomes user displaying current date'''
        self.clear()
        self.current_date = date.today()
        print(f'Todays date: {self.current_date}')
        print('Welcome to the budget manager' + '\n')

    def get_user(self):
        '''recieves user name as input string and return it
        to be used for file handling'''
        self.user_name = input('What is your name: ')
        return self.user_name

    def get_amount(self):
        self.clear()
        '''recives amount to be used for budget creation in string format'''
        print('\nYou chose to create a budget based on a new income amount')
        print('Please follow these instructions:\n')

        print('ONLY USE "." FOR CENTS IF NEEDED, DO NOT USE ","')
        self.new_amount = (input('Please input the amount here: $'))
        return self.new_amount

    def get_date(self):
        self.clear()
        '''receives date in string format,
        this date will be used to retrieve previous budget'''
        print('USE THE FOLLOWING DATE FORMAT YYYY-MM-DD')
        self.new_date = input(
            'Please input the date of your reported income to see budget: ')
        return self.new_date

    def display_budget_header(self, new_date):
        self.clear()
        '''displays current date and budget of given date'''
        print(f'Current date: {self.current_date}')
        print(f'Budget of income received on: {new_date}')

    def select_options(self):
        '''ask user what to do and return users selection as a string'''
        print('Press "p" to see a previous budget given based on the income date')
        print('Press "b" to create a budget based on new income')
        print('Press "e" to exit')
        self.user_selection = input('What would you like to do?: ')
        return self.user_selection
    
    def clear(self):
        '''clears screen using os module'''
        os.system('cls' if os.name == 'nt' else 'clear') # this clears the console
