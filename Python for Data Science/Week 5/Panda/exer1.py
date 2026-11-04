import pandas as pd

data = {
    'Product' : ["Asus",'Dell','Macbook','Lenovo','Alien'],
    'Quantity' : [10,25,15,12,30],
    'Price' : [800,500,300,250,50]
}

df = pd.DataFrame(data)
df['Revenue'] = df['Quantity'] * df['Price']


print(df)
print("")

#Highest Revenue
print('Highest Revenue Product is', df['Revenue'].max())
print('')

#Total Revenue
print("Total Revenue is", df['Revenue'].sum())
print('')

# Avg Quantity
print('Average Quantity', df['Quantity'].mean())
print('')

# Product Quantity Greater than 15
print('Product quantity greater than 15 is', df.loc[df['Quantity'] > 15, 'Product'] )

# Sort Highest to Lowest by revenue
print('Highest to Lowest by Revenue is ', df['Revenue'].sort_values(ascending=False))

