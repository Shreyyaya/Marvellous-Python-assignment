import numpy as np
import pandas as pd

data = {
    'Name': ['Amit', 'Sagar' ,'Pooja'],
    'Math' : [85, 90, 78],
    'Science' : [92, 88, 85],
    'English' : [78 ,80, 82],
    
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()

Gender = ['Male', 'Male', 'Female']

df = pd.DataFrame(data)

df['Gender'] = Gender

group = df.groupby('Gender')
print(df)

average = df.mean(numeric_only=True)
print(average)
