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

marks = df[df['Name']== 'Sagar'][['Math', 'Science', 'English']].values.flatten()

subjects = ['Math', 'Science', 'English']

plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title("Sagar report Piechart")
plt.grid(True)
plt.show()