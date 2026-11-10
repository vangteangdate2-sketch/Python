# main.py
# Import the custom automation function you just built!
from excel_helper import manage_excel
import pandas as pd

# Configuration setup
MY_FOLDER = r"C:\Users\ASUS\Documents\Excel File"
MY_FILE = "MyEmployeeBetter.xlsx"
MY_SHEET = "Employees"

# --- CASE A: Save a fresh database (Overwrite) ---
initial_employees = {
    "Name" : ['Lina','Kanha','Bopha'],
    "Age"  : [12, None, 32],
    "City" : ['Phnom Penh','Kampong Cham','Kampot'],
    "Salary": [500, 300, 500]
}

# Run the automation in 'overwrite' mode
manage_excel(initial_employees, MY_FOLDER, MY_FILE, MY_SHEET, mode="overwrite")


# --- CASE B: Add a new hire later in the code (Append) ---
#new_hire = {
#     "Name" : ['Dara'],
#    "Age"  :['20'],
#    "City" : ['Battambang'],
#    "Salary": [450]
#}

# Re-use the exact same function, just switch mode to 'append'!
#manage_excel(new_hire, MY_FOLDER, MY_FILE, MY_SHEET, mode="append")

df = pd.DataFrame(initial_employees)

print(df)


