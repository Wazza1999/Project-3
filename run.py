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
def input_name_data():

    while True:
        first_name = input("Please enter your first name:")
        last_name = input("Please enter your last name:")
        if first_name.isalpha():
            print("\nHello", first_name,last_name, "Welcome to Warrens Kitchens' Database:\n")
            return 
    else:
        print("Please do not input invalid characters such as numbers.")


"""
Input position of company
"""
def get_position_data():
    print("Please select your current position in the company from the following roles:\n")
    positions = ["Head Chef", "Sous Chef", "Chef de Partie", "Commis Chef", "Kitchen Porter"]
    print('\n'.join(positions))
    yes = ["Y"]
    while True:
        position = input("\nEnter Role Here:")
        if position in positions:
            print("You selected:", position)
            yes = input("Is that correct Y/N:")
        if yes == "Y":
            return position
        else:
            print("Incorrect data inputted, please select correct role.")

"""
Show previous the hours worked in the previous week.
"""
def get_previous_data(position):
    yes = ["Y"]
    no = ["N"]
    while True:
        yes = input("Would you like to see the hours you worked last week? Y/N:")
        if yes == "Y":
            print("\nHere are you total hours from last week:", position)
            previous = SHEET.worksheet("previous").get_all_values()
            
            positions = previous[0]  
            position_col = positions.index(position)  

            last_row = previous[-1]  
            total_hours = last_row[position_col]  

            print("\nTotal hours for position:", total_hours)
        elif "N":
            print("\nContinuing....\n")
            break
        else:
            print("\nInvalid input, please only use Y/N")
            print("\nReturning to question.")
    
"""
Allow user to input their data for the current week and have it totalled
"""
def get_user_data():

    print("Please enter days you have worked" )
    print("Only add data up to 7 days.")
    print("Example: 1,2,3,4,5,6,7\n")
    number_str = input("Enter data here:")
    current_data = data_str.split(",")

    if validate_data(sales_data):
        while True:
            try:
                number = int(number_str)
                print(f"You entered {number}")
            except ValueError:
                print("This is not a number or there are too many numbers. Please enter data up to 7 days.")
        

    """
    Runs all program functions
    """
def main():
    name = input_name_data()
    position = get_position_data()
    previous = get_previous_data(position)
    user = get_user_data()
    
print("Welcome to Warrens Kitchens' Database")
main()  

