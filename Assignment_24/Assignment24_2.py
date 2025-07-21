import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    'Name': ['Amit', 'Sagar' ,'Pooja'],
    'Math' : [85, 90, 78],
    'Science' : [92, 88, 85],
    'English' : [78 ,80, 82]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()

Gender = ['Male', 'Male', 'Female']

df = pd.DataFrame(data)

df['Gender'] = Gender

print(df)

encode = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
data_encoded = encode.fit_transform(df[['Gender']])
df_encoded = pd.DataFrame(data_encoded, columns=encode.get_feature_names_out(['Gender']))

print("Encoded DataFrame:")
print(df_encoded)

