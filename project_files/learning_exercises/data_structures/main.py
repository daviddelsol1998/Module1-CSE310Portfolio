'''This file will be used to explore data structures within Python'''
import pandas as pd
from datetime import date

# get user input 3 times
amounts = {'Date':[],'Amount':[]}
# #create df
# df = pd.DataFrame.from_dict(amounts)
# df.to_csv('amounts_bydate.csv')


for i in range(3):
    user_input = input('Please enter amount: ')
    now_date = date.today()
    amounts['Date'].append(now_date)
    amounts['Amount'].append(user_input)

print(amounts)

#create df
df = pd.DataFrame.from_dict(amounts)
df.to_csv('amounts_bydate.csv', mode='a', index=False, header= False)


