'''This is the main module that runs the entire program.
This was also used to test each indidividual module for 
correct functionality'''

from interface import UserInterface
from file_manager import FileManager
from budget_generator import BudgetGenerator

bg = BudgetGenerator('1000')
bg.generate_budget()
print(bg.budget)

