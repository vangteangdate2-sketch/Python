import pandas as pd

data = {
    "Name" : ['Dara','Sokha','Nika'],
    "Age" : [20,12,43],
    'Score' : [85,34,94]
}

df = pd.DataFrame(data)

print(df[['Name','Score','Age']])