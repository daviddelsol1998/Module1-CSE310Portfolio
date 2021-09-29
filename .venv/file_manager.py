'''This module handles all of the functionality of the file manager
in order to acomplish all these functions, the pandas library is used to read, create
and update csv files with ease'''
import pandas as pd  # library used to work with csv files
from os.path import exists  # used to see if a file exists.


class FileManager:
    '''This class inherits base functionality from pandas library to work on csv files.
    argument required to initialize class FileManager(file_given): file given = username
    the class has 4 functions, to 
    1) create a filecheck: def create_file(),
    2) check if a file exist: file_exist(), and if so 
    3) read said file by date given to return budget: get_budget_by_date(date_given), 
    4) update file with the following information:
    def update_file(date_given, income_given, tithing_given, savings_given, spending_balance_given)'''

    def __init__(self, file_given):
        '''this initializes the class with one argument (username) to be used as file name'''
        self.file_given = file_given
        self.file_format = {
            'date': [],
            'income': [],
            'tithing': [],
            'savings': [],
            'spending_balance': []
        }

    def create_file(self):
        '''this method is called to create a file with (file_given = username)
        if the file doesn't exist'''
        df = pd.DataFrame(self.file_format)
        df.to_csv(f'{self.file_given}.csv')

    def file_exist(self):
        '''this returns true or false to indicate
        whether a file exist or not'''
        return exists(f'{self.file_given}.csv')

    def update_file(self, date_given, income_given, tithing_given, savings_given, spending_balance_given):
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
        budget = pd.read_csv(f'{self.file_given}.csv')
        print(budget[budget.date == date_given])
