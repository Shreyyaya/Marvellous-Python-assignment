import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
df = pd.DataFrame(data)


df['Grade'] = df['Grade'].replace({'A+': 'Excellent','A': 'Very Good', 'B+': 'Good', 'B': 'Average', 'C': 'Poor'})
print(df)