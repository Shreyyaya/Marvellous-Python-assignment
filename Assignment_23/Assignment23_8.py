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

marks = df[df['Name']== 'Amit'][['Math', 'Science', 'English']].values.flatten()

subjects = ['Math', 'Science', 'English']

plt.plot(subjects, marks, marker = 'o')
plt.xlabel("subjects")
plt.ylabel("marks")
plt.title("amit report lineplot")
plt.grid(True)
plt.show()