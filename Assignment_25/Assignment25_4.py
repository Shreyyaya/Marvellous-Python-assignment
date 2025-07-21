import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
df = pd.DataFrame(data)

dept_encoded = pd.get_dummies(df, columns = ['Department'])
print(dept_encoded)