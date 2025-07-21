import pandas as pd
import numpy as np


data = {'Marks': [45, 67, 88, 32, 76]}


df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()

df['Marks'] = np.where(df['Marks'] < 50, 'Fail', df['Marks'])
print(df)
