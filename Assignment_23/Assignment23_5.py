import pandas as pd
import numpy as np

data = {
'Name': ['Amit', 'Sagar' ,'Pooja'],
'Math' : [85,90,78],
'Science' : [92, 88, 85],
'English' : [ 78 ,80,82]
}

df = pd.DataFrame(data)

df['Name'] = df['Name'].replace('Pooja', 'Puja')
print(df)