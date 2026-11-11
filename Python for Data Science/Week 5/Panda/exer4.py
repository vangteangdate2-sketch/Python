import pandas as pd

data = {
    "CustID": ["C001", "C002", "C003", "C004", "C005", "C005"],
    "Name": ["Dara", "Sokha", "Lina", "Bora", "Vanna", "Vanna"],
    "Age": [22, 25, None, 28, 150, 28],
    "City": ["Phnom Penh", "PHNOM PENH", "Siem Reap", "PP", "Phnom Penh", "Phnom Penh"],
    "Income": [500, 700, 600, None, 800, 800]
}

df = pd.DataFrame(data)

#remove duplication
df = df.drop_duplicates()

#remove any outlier not more than 100 years old
df = df[(df["Age"] >= 0) & (df["Age"] <= 100)]

#handle any missing values
df["Age"] = df["Age"].fillna(df["Age"].median())

# fill miss information
df['Income'] = df['Income'].fillna(df['Income'].mean())

#standardize the data
df["City"] = df["City"].str.lower().str.strip()

df["City"] = df["City"].replace({
    "pp": "phnom penh",
    "phnom-penh": "phnom penh"
})

df["City"] = df["City"].str.title()

print(df)

