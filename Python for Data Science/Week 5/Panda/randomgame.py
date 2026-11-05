import pandas as pd

data = {
    'Name': ['dara','cheata','panha'],
    'sex' : ['M','F','M'],
    'score' : [80,98,89]
}

df = pd.DataFrame(data)
df['age'] = [19,20,21]
df['status'] = df['score'] <= 50


print(df)
print('')
print(df[df['score']>50])
print('')

print('ascending false is ', df.sort_values('score',ascending=True))