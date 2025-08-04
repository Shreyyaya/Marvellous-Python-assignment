import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = load_breast_cancer()
    print("Independent (Features) var names are: ")
    print(df.feature_names)
    print()

    print("Dependent (labels) var names are: ")
    print(df.target_names)

    data = pd.DataFrame(df.data, columns=df.feature_names)

    data['diagnosis'] = df.target  # adding diagnosis column (0 = malignant, 1 = benign) as target

    print(data.head())

    x = data.drop('diagnosis', axis=1)
    y = data['diagnosis']


    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)


    X_train, X_test, Y_Train, Y_Test = train_test_split(x_scaled, y, test_size = 0.2, random_state= 42)

    model = LogisticRegression()

    model.fit(X_train, Y_Train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_Test, Y_pred)
    print("Accuracy is: ", accuracy*100)

    Con_mat = confusion_matrix(Y_Test, Y_pred)
    print("Confusion matrix is: ")
    print(Con_mat)

    Report = classification_report(Y_Test, Y_pred)
    print("classification report is: ")
    print(Report)

    correlation_matrix = data.corr()

    plt.figure(figsize=(14, 12))    #EDA
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='Blues')

    plt.title('Correlation Matrix of Breast Cancer Features')
    plt.tight_layout()    #if we use legend then the values dont fit in the box
    plt.show() 


if __name__ == "__main__":
    main()
