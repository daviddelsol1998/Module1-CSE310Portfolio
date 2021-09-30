from file_manager import FileManager
from interface import UserInterface

fm = FileManager('Carlos')
fm.get_budget_by_date('2021-09-31')
ui = UserInterface()
print(ui.current_date.strftime('%Y-%m-%d'))