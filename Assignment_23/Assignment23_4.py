import pandas as pd
import numpy as np

data = {
'Name': ['Amit', 'Sagar' ,'Pooja'],
'Math' : [85,90,78],
'Science' : [92, 88, 85],
'English' : [ 78 ,80,82]
}

df = pd.DataFrame(data)

print("Students who scored more than 85 in science: ")
print(df[df['Science']>85])