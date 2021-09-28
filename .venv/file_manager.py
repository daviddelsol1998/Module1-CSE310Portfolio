'''This module handles all of the functionality of the file manager
in order to acomplish all these functions, the pandas library is used to read, create
and update csv files with ease'''
import pandas as pd  # library used to work with csv files
from os.path import exists  # used to see if a file exists.


class FileManager:
    '''This class inherits base functionality from pandas library to work on csv files.
    the class has 4 functions, to check if a file exist, and if so to create, to read said file'''

    def __init__(self, file_given):
        '''this initializes the class with one argument (file name to work on)'''
        self.file_given = file_given
        self.file_format = {
            'date': [],
            'income': [],
            'tithing': [],
            'savings': [],
            'spending_balance': []
        }

    def create_file(self):
        '''this method is called to create a file if the file doesn't exist'''
        df = pd.DataFrame(self.file_format)
        df.to_csv(f'{self.file_given}.csv')

    def file_exist(self):
        '''this returns true or false whether a function exist or not'''
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
        df.to_csv(f'{self.file_given}.csv', mode='a',
                  index=False, header=False)
