'''This is the main module that runs the entire program.
This was also used to test each indidividual module for 
correct functionality'''

# import all module dependencies
from interface import UserInterface
from file_manager import FileManager
from budget_generator import BudgetGenerator
import sys  # to be used in killing the program early

# greet user
ui = UserInterface()
# save current day used to check if a budget has been generated
current_day = ui.current_date.strftime('%Y-%m-%d')  # used for string formating

real_user = False

while not real_user:
    # get user name
    user = ui.get_user()

    # initiate file manager with possible user
    fm = FileManager(user)

    # check if user exist
    if not fm.file_exist():
        print('user does not exist.')

        # ask if you'd like to create an user with that name
        print('\npress "y" for yes or "n" for no, or type "e" to exit.')
        new_user = input(
            f'Would you like to create an user with the name of "{user}"?: ')
        new_user = new_user.capitalize()  # for all caps performance

        # check user input
        if new_user == 'Y':
            fm.create_file()
            real_user = True
        elif new_user == 'N':
            print('\nPlease make sure you check your name spelling and try again.')
        elif new_user == 'E':
            print('Okay bye...')
            sys.exit()  # kills the program
        else:
            print('\nThat was not "y" or "n". Try again.')

    else:
        print(f'\nWelcome {user}\n')
        real_user = True
        input('Press any key to continue')

# initialize file manager with real user
fm = FileManager(user)

done = False

while not done:
    # check user choice
    ui.clear()  # clear screen
    print('What would you like to do?\n')
    user_choice = ui.select_options()
    user_choice = user_choice.capitalize()  # for all caps performance

    # handle create budget based on new income
    if user_choice == "B":
        # check if a budget has been created today already
        if current_day in fm.read_file().values:  # file contents
            ui.clear()  # clear screen
            print('\nA budget has already been generated today')
            print('Please upgrade to premium version for more than one budget per day')
            input('Press any key to continue')
        else:
            # get amount to create
            new_income = ui.get_amount()
            # generate budget based on new_income
            bg = BudgetGenerator(new_income)
            budget = bg.generate_budget()
            # update file
            print('\nCreating budget and saving it in file')
            fm.update_file(
                ui.current_date, budget['income'], budget['tithing'], budget['savings'], budget['spending'])
            # display generated budget
            ui.display_budget_header(ui.current_date)
            fm.get_budget_by_date(current_day)
            input('Press any key to continue')
    # handle check budget based on date
    elif user_choice == "P":
        # get date of the budget user would like to see
        previous_date = ui.get_date()
        # get budget by that date
        ui.display_budget_header(previous_date)
        fm.get_budget_by_date(previous_date)
        done = True
    # exit
    elif user_choice == "E":
        print('Okay bye...')
        sys.exit()  # kills the program
    else:
        print('That is not a valid option')

