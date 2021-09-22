'''the purpose of this file is to explore the read and write capabilities of python
for my budget program.'''

'''for the first experiment, I will explore the procedure of reading and writing files
using open and read and write functions within open'''
for i in range(3):  # prompt user for 3 numbers
    # save user input in variable
    user_input = input('Please enter a number: ')
    with open('numbers.txt', mode='a', ) as numbers_file:  # open file for appending
        numbers_file.write(user_input + '\n')  # append input into the file


# print each number in numbers.txt
with open('numbers.txt', mode='r') as numbers_file:  # open file for reading
    print(numbers_file.readlines())  # returning list of numbers



