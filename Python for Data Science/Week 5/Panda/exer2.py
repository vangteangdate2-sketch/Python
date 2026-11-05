import pandas as pd

data = { "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",'OverDay'],
         "Orders": [100, 120, 90, 150, 180, 220, 200, 3000],
         "Revenue": [2000, 2400, 1800,3000, 3600, 4400, 4000, 2000]
}

df = pd.DataFrame(data)

print(df)
print('')

print("Highest Sales of the Week is ", df.loc[df['Revenue'].idxmax(), 'Day'])
print('')

print('Avg Number of Order is', df['Orders'].mean())
print('')

print('Days have more than 150 orders of the this is', df.loc[df['Orders'] > 150, 'Day'].tolist())
print(' ')

print('Total Revenue of this overall day', df['Revenue'].sum())
print('')