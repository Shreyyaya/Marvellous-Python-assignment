
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

def main():
    df = pd.read_csv("Diabetes.csv")

    print(df.columns)
    print(df.head())
    print(df.describe())

    null_values = df.isnull().sum()
    print(null_values)         #handling missing?null values if any


    x = df.drop(columns = ['Outcome'])
    y = df['Outcome']
    
    plt.figure(figsize=(8, 6))
    sns.countplot(x = y)
    plt.title('Distribution of Outcome')
    plt.xlabel('Outcome')
    plt.ylabel('Count')
    plt.show()             #distribution of the outcomes

    numeric_col = df.select_dtypes(include='number').columns   #considering columns which have numeric values in them

    for col in numeric_col:
        if col != 'Outcome':
            plt.figure(figsize=(6, 4))
            sns.boxplot(x="Outcome", y=col, data=df, palette="pastel")
            plt.title("Boxplot of respective column by Outcome")
            plt.xlabel("Outcome")
            plt.ylabel(col)
            plt.tight_layout()
            plt.show()                  # a loop to plot the outcome with respective columns present in the dataset


    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)    #scaling the independent variables


    x_train, x_test, y_train , y_test = train_test_split(x_scaled, y, test_size= 0.2, random_state=42)

    log_clf = LogisticRegression()  #logistic classifier
    dt_clf = DecisionTreeClassifier(max_depth=8)  # we can change value of max_depth and n_neighbors

    voting_clf = VotingClassifier(
        estimators= [
            ('lr', log_clf),
            ('dt', dt_clf),   
        ],
        voting= 'hard'    #voting ='soft' is other option
    )

    voting_clf.fit(x_train, y_train)

    y_pred = voting_clf.predict(x_test)

    print(accuracy_score(y_pred, y_test)*100)   #accuracy 

    class_report = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(class_report)

    con_mat = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(con_mat)

    plt.figure(figsize=(6, 5))
    sns.heatmap(con_mat, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1], yticklabels=[0, 1])
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.show()                 #plotting confusion matrix in heatmap format

if __name__ == "__main__":
    main()        