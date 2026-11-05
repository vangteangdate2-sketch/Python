import pandas as pd

data_scores = pd.read_csv(r'c:\Users\ASUS\Downloads\Telegram Desktop\student_scores.csv')

data_scores.rename(columns= {
    'gender' : 'sex',
    'city' : 'fishy'
})

data_scores.loc[data_scores['city'] == 'Kampot','city'] = 'KomPot'

print(data_scores)
