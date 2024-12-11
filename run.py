import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import pandas as pd


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Project-3')

"""
Input your first and last name.
"""
while True:
    first_name = input("Please enter your first name:")
    last_name = input("Please enter your last name:")
    if first_name.isalpha():
        print("\nHello", first_name,last_name, "Welcome to Warrens Kitchens' Database:\n")
        break
    else:
        print("Please do not input invalid characters such as numbers.")


"""
Input position of company
"""
print("Please select your current position in the company from the following roles:\n")
positions = ["Head Chef", "Sous Chef", "Chef de Partie", "Commis Chef", "Kitchen Porter"]
print('\n'.join(positions))
while True:
    position = input("\nEnter Role Here:")
    if position in positions:
        print("You selected:", position, first_name,)
        yes = input("Is that correct Y/N:")
    if yes == "Y":
        break
    else:
        print("Please select correct role.")

"""
Show previous the hours worked in the previous week.
"""
yes = ["Y"]
no = ["N"]
while True:
    yes = input("Would you like to see the hours you worked last week? Y/N:")
    if yes == "Y":
        print("Here are you total hours from last week:", position)
        previous = SHEET.worksheet("previous").get_all_values()

        positions = previous[0]  
        position_col = positions.index(position)  

        last_row = previous[-1]  
        total_hours = last_row[position_col]  

        print("Total hours for position:\n ", total_hours)
        break
    
  

