import pandas as pd
import numpy as np

data =  {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}
df = pd.DataFrame(data)

print("before: ")
print(df)
print()

df['Age']= df['Age'].astype(int)
print("After:")
print(df)