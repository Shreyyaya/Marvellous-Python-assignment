import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
'Name': ['Amit', 'Sagar' ,'Pooja'],
'Math' : [85,90,78],
'Science' : [92, 88, 85],
'English' : [ 78 ,80,82]
}

df = pd.DataFrame(data)
print(df)

model = MinMaxScaler()

df[['Math']]=model.fit_transform(df[['Math']])
print(df)