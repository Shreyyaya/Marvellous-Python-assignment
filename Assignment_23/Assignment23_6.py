import pandas as pd
import numpy as np

data = {
'Name': ['Amit', 'Sagar' ,'Pooja'],
'Math' : [85,90,78],
'Science' : [92, 88, 80],
'English' : [ 78 ,85,82]
}

df = pd.DataFrame(data)

df['Total']= df['Math'] + df['Science'] + df['English']

print("Before sorting")
print(df)

df_new = df.sort_values(by = 'Total', ascending = False)
print("After sorting")
print(df_new)