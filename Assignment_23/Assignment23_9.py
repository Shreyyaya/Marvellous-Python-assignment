import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data2 = {
'Name': ['Amit', 'Sagar' ,'Pooja'],
'Math' : [np.nan,76,88],
'Science' : [91, np.nan, 85],

}

df = pd.DataFrame(data2)


print("Before: ")
print(df)

df.fillna(df.mean(numeric_only= True), inplace = True)

print("After: ")
print(df)