'''This module handles all of the functionality of the file manager
in order to acomplish all these functions, the pandas library is used to read, create
and update csv files with ease'''
from os import path
import pandas as pd


class FileManager:
    '''This class inherits base functionality from pandas library to work on csv files.
    the class has 4 functions, to check if a file exist, and if so to create, to read said file'''

    def __init__(self, file_given):
        '''this initializes the class with one argument (file name to work on)'''
        self.file_given = file_given

    def create_file(self):
        '''this method is called to create a file if the file doesn't exist'''
        empty_file_format = {
            'Date': [],
            'income': [],
            'tithing': [],
            'savings': [],
            'spending_balance': []
        }

        df = pd.DataFrame(empty_file_format)
        df.to_csv(f'{self.file_given}.csv')
        
