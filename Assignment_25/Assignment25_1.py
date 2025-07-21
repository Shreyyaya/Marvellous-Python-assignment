import pandas as pd
import numpy as np

data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
df = pd.DataFrame(data)

def IQR_Method(datapath, column):
    q1 = datapath[column].quantile(0.25)
    q3 = datapath[column].quantile(0.75)
    IQR = q3 - q1

    LowerBound = q1 - 1.5*IQR
    UpperBound = q3 + 1.5*IQR

    outliers = datapath[(datapath[column] < LowerBound) | (datapath[column] > UpperBound)]
    return outliers

def main():
    outliers = IQR_Method(df, 'Salary')
    print("Outliers are:\n", outliers)

if __name__ == "__main__":
    main()
