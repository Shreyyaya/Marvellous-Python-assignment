import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Amit', 'Sagar' ,'Pooja'],
    'Math' : [85, 90, 78],
    'Science' : [92, 88, 85],
    'English' : [78 ,80, 82],
    
}

df = pd.DataFrame(data)

df = df.rename(columns= {'Math': 'Mathematics'})
print(df)