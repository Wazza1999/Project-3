import gspread
from google.oauth2.service_account import Credentials
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
def get_name_data():

    while True:
        first_name = input("Please enter your first name:")
        last_name = input("Please enter your last name:")
        if first_name.isalpha():
            print("\nHello", first_name, last_name, "Welcome to Warrens Kitchens' Database:\n")
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
    no = ["N"]
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
            return position
        elif "N":
            print("\nContinuing....\n")
            break
        else:
            print("\nInvalid input, please only use Y/N")
            print("\nReturning to question.")
    
"""
Allow user to input their data for the current week and have it totalled
Used Love sandwiches walkthrough for this bit of code as I couldn't figure it out
"""
def get_user_data():
    while True:
        print("Please enter days you have worked" )
        print("Only add data up to 7 days.")
        print("Example: 1,2,3,4,5,6,7\n")
        
        data_str = input("Enter data here:")
        
        current_data = data_str.split(",")

        if validate_data(current_data):
            print("\nData is Valid...\n")
            break

"""
Converts all string values into integers. 
Raises ValueError if strings cannot be converted into int,
or if there aren't exactly 7 values.
Used Love sandwiches walkthrough for this bit of code as I couldn't figure it out 
"""
def validate_data(values):
    try:
        [int(value) for value in values]
        if len(values) !=7:
            raise ValueError(
                f"Exactly 7 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True
    
"""
Updates the worksheet with the users inputted data
"""
def update_current_worksheet(name):
    print("Updating the worksheet with your hours worked.\n")
    print("Thank you for inputting the data.\n")
    current_worksheet = SHEET.worksheet("current")
    current_worksheet.append_row(name)

    print("Closing program...")

    """
    Runs all program functions
    """
def main():
    name = get_name_data()
    position = get_position_data()
    previous = get_previous_data(position)
    user = get_user_data()
    update_current_worksheet(name)
print("Welcome to Warrens Kitchens' Database")
main()  
