import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
'Name': ['Amit', 'Sagar' ,'Pooja'],
'Math' : [85,90,78],
'Science' : [92, 88, 80],
'English' : [78,85,82]
}

df = pd.DataFrame(data)

df_updated = df.drop(columns = ['English'])

print(df_updated)
