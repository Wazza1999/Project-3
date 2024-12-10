import gspread
from google.oauth2.service_account import Credentials


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
first_name = input("Please enter your first name:")
last_name = input("Please enter your last name:")

print("Hello", first_name,last_name, "Welcome to Warrens Kitchens' Database:\n")

"""
Input position of company
"""
print("Please select your current employed role in the company:")



