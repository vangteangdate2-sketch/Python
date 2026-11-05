import pandas as pd

df = pd.read_excel(r"C:\Users\ASUS\Downloads\Book1.xlsx")

print(df)
print('')

#total price
df['Total Price'] = df['Quantity'] * df['Price']
print(df)
print('')

#find orders above $500
print(df.loc[df['Total Price'] > 500])
print('')

#sort by total price
print(df.sort_values(by='Total Price',ascending=False))
print('')

#calculate the sum of total price
print('sum of total price', df['Total Price'].sum())

#calculate the average of total price
print('sum of average price', df['Total Price'].mean())