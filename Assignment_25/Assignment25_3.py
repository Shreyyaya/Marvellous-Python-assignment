import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
df = pd.DataFrame(data)

label_encoder = LabelEncoder()

df['City_encoded'] = label_encoder.fit_transform(df['City'])
print(df)