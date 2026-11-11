import pandas as pd

# Create the data from the image
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Category': ['Electronics', 'Electronic', 'Electronics', 'Electronic'],
    'Price': ["$1200", "$25", "$50", "$300"],
    'Sales': [10, 50, 30, 15]
}

df = pd.DataFrame(data)
print(df)

# Step 0: Clean Category column (standardize to 'Electronics')
df['Category'] = 'Electronics'
df['Price'] = df['Price'].str.replace('$', '', regex=False).astype(float)

# Step 1: Calculate Revenue for each row
df['Revenue'] = df['Price'] * df['Sales']

total_revenue = df['Revenue'].sum()
avg_price = df['Price'].mean()

print(f"Total Revenue: {total_revenue}")
print(f"Average Price: {avg_price}")

# Step 2: Revenue by category
rev_by_cat = df.groupby('Category')['Revenue'].sum()
print(rev_by_cat)

print()
