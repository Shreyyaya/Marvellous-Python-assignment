import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
df = pd.DataFrame(data)
print(df)

x = df[['Age']]
y = df[['Purchased']]

x_train,x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("X_train shape: ", x_train.shape)
print("X_test shape: ", x_test.shape)
print("y_train shape: ", y_train.shape)
print("Y_test shape: ", y_test.shape)