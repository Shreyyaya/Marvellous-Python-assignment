import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = {'Age': [18, 22, 25, 30, 35]}
df = pd.DataFrame(data)
print("Data before min-max scaling: ")
print(df)
print()

model = MinMaxScaler()

df[['Age']]=model.fit_transform(df[['Age']])
print("Data after min-max scaling: ")
print(df)