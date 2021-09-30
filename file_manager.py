'''This module handles all of the functionality of the file manager
in order to acomplish all these functions, the pandas library is used to read, create
and update csv files with ease'''
import pandas as pd  # library used to work with csv files
from os.path import exists  # used to see if a file exists.


class FileManager:
    '''This class inherits base functionality from pandas library to work on csv files.
    argument required to initialize class FileManager(file_given): file given = username
    the class has 5 functions, to 
    1) create_file(): create a csv file with (file_given = username), only to be called if file doesn't exist.
    2) file_exist(): this returns true or false to indicate whether a file exist or not. 
    3) get_budget_by_date(date_given): read said file by date given to return budget.
    4) update_file(date_given, income_given, tithing_given, savings_given, spending_balance_given):
    update file with the following information:
    5) read_file : just return file as pd format for values comparison
    '''

    def __init__(self, file_given):
        '''This initializes the class with one argument (username) to be used as file name.
        it creates an empty file format that will be hold on file format attribute'''
        self.file_given = file_given
        self.file_format = {
            'date': [],
            'income': [],
            'tithing': [],
            'savings': [],
            'spending_balance': []
        }

    def create_file(self):
        '''create a csv file with (file_given = username), only to be called if file doesn't exist.'''
        df = pd.DataFrame(self.file_format)
        df.index.name = 'Budget'
        df.to_csv(f'{self.file_given}.csv')

    def file_exist(self):
        '''this returns true or false to indicate
        whether a file exist or not'''
        return exists(f'{self.file_given}.csv')

    def update_file(self, date_given, income_given, tithing_given, savings_given, spending_balance_given):
        '''this method is used to update the contents of a file by adding the following information as 
        parameters from the budget generator'''
        # update dictionary
        self.file_format['date'].append(date_given)
        self.file_format['income'].append(income_given)
        self.file_format['tithing'].append(tithing_given)
        self.file_format['savings'].append(savings_given)
        self.file_format['spending_balance'].append(spending_balance_given)

        # update file
        df = pd.DataFrame.from_dict(self.file_format)
        df.to_csv(f'{self.file_given}.csv', mode='a', header=False)

    def get_budget_by_date(self, date_given):
        '''This returns the budget from the csv file based on a date given as an argument'''
        budget = pd.read_csv(f'{self.file_given}.csv')
        # check if date exist
        if date_given in budget.values:
            print('\n')
            print(budget[budget.date == date_given])
        else:
            print('\nDate does not exist in file')

    def read_file(self):
        '''just return file as pd format for values comparison'''
        return pd.read_csv(f'{self.file_given}.csv')