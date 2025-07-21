import pandas as pd
import numpy as np

data = {
'Name': ['Amit', 'Sagar' ,'Pooja'],
'Math' : [85,90,78],
'Science' : [92, 88, 85],
'English' : [ 78 ,80,82]
}

df = pd.DataFrame(data)
print("shape of dataframe is: ", df.shape)
print("Column information of dataframe is:",df.columns)
print("Datatype is: ",df.dtypes)