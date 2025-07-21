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
print(df)

plt.hist(df['Math'], bins=3, color='skyblue', edgecolor='black')

plt.xlabel('Math marks')
plt.ylabel('Students')
plt.title('Distribution of math marks')
plt.show()
