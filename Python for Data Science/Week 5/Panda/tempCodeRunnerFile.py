import pandas as pd

df = pd.read_excel(r"C:\Users\ASUS\Downloads\Book1.xlsx")

print(df)
print('')

#total price
df['Total Price'] = df['Quantity'] * df['Price']
print('total price is ', df)
print('')

#find orders above $500
print('above $500 is ', df[df['Total Price'] > 500])
print('')

#sort by total price
print('Sorted by total price', df.sort_values(by='Total Price',ascending=False))
print('')

#calculate the sum of total price
print('sum of total price', df['Total Price'].sum())

#calculate the average of total price
print('sum of average price', df['Total Price'].mean())