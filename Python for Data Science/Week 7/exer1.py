import pandas as pd

students = {
    "Student_ID" : ["101", "102", "103", "104",'Student ID'],
    "Student Name" : ["  dara sok ", "SOK DARA  ", " chantha", "Vannak ", 'Student Name'],
    "Email" : ["DARA@GMAIL.COM", "sok@gmail.com", "CHAN@GMAIL.COM", "vannak@gmail.com",'Email'],
    "Department" : ["computer science", "IT", "COMPUTER SCIENCE", "it",'Department']
}

df = pd.DataFrame(students)


# Unnecessary Name
df["Student Name"] = df["Student Name"].str.strip()
df["Student Name"] = df["Student Name"].str.capitalize()


#Emails use different letter cases
df["Email"] = df["Email"].str.lower()
df["Email"] = df["Email"].str.capitalize()


# Department name are inconsistent
df['Department'] = df['Department'].str.title()
df["Department"] = df["Department"].replace({"It": "IT", "Computer Science": "Computer Science"})

# Remove
df = df[df["Student_ID"] != "Student ID"]
df = df[df["Student Name"] != "Student Name"]
df = df[df["Email"] != "Email"]
df = df[df["Department"] != "Department"]

print(df)

