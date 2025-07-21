import pandas as pd
import numpy as np


data = {'Marks': [85, np.nan, 90, np.nan, 95]}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()


df_interpolation = df.interpolate()
print("DataFrame after linear interpolation: ")
print(df_interpolation)