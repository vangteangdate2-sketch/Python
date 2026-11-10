import os
import pandas as pd

# 1. Use an 'r' before the quotes to handle the Windows backslashes properly
folder_path = r"C:\Users\ASUS\Documents\Excel File"
file_name = "MyEmployee.xlsx"

# 2. Combine them into a secure file path
excel_filepath = os.path.join(folder_path, file_name)

# Your target data
data = {
    "Name": ["Lina", "Kanha", "Bopha", "Sokha", "Bora"],
    "Age": [12, None, 32, 12, 43],
    "City": ["Phnom Penh", "Kampong Cham", "Kampot", "Siem Reap", "PP"],
    "Salary": [500, 300, 500, 300, None],
}

# STEP 1: Check and Save (Protects your file from overwriting)
if os.path.exists(excel_filepath):
    print(f"📢 File already exists in Documents. Leaving it exactly as it is.")
else:
    print(f"🆕 Saving fresh file directly to your Documents folder...")
    df_export = pd.DataFrame(data)
    df_export.to_excel(excel_filepath, sheet_name="Employees", index=False)


# STEP 2: Read from your Documents folder
print(f"\n--- Reading Data from: {excel_filepath} ---")
df_import = pd.read_excel(excel_filepath, sheet_name="Employees")
print(df_import)
