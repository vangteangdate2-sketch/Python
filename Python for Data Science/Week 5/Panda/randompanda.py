import pandas as pd

scores = pd.Series([80,76,54,243,65])
print(scores)

scores = pd.Series([80,76,54], index =['Dara','Sokha','Rina'])

print(scores)
print("mean is ", scores.mean())
print("median is ", scores.median())
print("mode is ", scores.mode())
print("standard deviation is ", scores.std())
print("sum is ", scores.sum())

print(scores>75)
