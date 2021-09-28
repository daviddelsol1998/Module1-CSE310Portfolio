'''This is the main module that runs the entire program.
This was also used to test each indidividual module for 
correct functionality'''

from interface import UserInterface
from file_manager import FileManager

ui = UserInterface()
fm = FileManager('David')
# fm.create_file()
# fm.update_file('04/21/2021',1000,100,100,800)
fm.get_budget_by_date('04/21/2021')







