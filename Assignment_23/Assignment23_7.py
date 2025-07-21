import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
'Name': ['Amit', 'Sagar' ,'Pooja'],
'Math' : [85,90,78],
'Science' : [92, 88, 80],
'English' : [ 78 ,85,82]
}

df = pd.DataFrame(data)

df['Total']= df['Math'] + df['Science'] + df['English']

print(df)

plt.bar(df['Name'], df['Total'])
plt.xlabel("Student names")
plt.ylabel("Total marks")
plt.title("Barplot")
plt.show()
