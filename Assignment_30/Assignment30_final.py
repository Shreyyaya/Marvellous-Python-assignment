import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, roc_auc_score, roc_curve, auc

def main():
    df = pd.read_csv("bank-full.csv", sep=';', quotechar='"')   #as the original dataset is with ; and with "" we need to specify them

    for col in df.select_dtypes(include='object'):
        df[col] = LabelEncoder().fit_transform(df[col])    #label encoding

    x = df.drop('y', axis=1)
    y = df['y']

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    x_train, x_test, y_train , y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

    log_clf = LogisticRegression()
    dt_clf = DecisionTreeClassifier(max_depth=8)

    voting_clf = VotingClassifier(
        estimators=[
            ('lr', log_clf), 
            ('dt', dt_clf)
            ],
        voting='soft'
    )

    voting_clf.fit(x_train, y_train)

    y_pred = voting_clf.predict(x_test)
    y_prob = voting_clf.predict_prob(x_test)[:, 1]  ##probabilities for positive class

    print(accuracy_score(y_test, y_pred) * 100)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    con_mat = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(con_mat)

    print("ROC AUC Score is:")
    print(roc_auc_score(y_test, y_prob))    #roc auc score

    plt.figure(figsize=(6, 5))
    sns.heatmap(con_mat, annot=True, fmt='d', cmap='Blue', xticklabels=[0, 1], yticklabels=[0, 1])
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.show()               #plotting of confusion matrix

    fpr, tpr, thresholds = roc_curve(y_test, y_prob)  #computation for roc curve   tpr = true positive rate   fpr = false positive rate
    roc_auc = auc(fpr, tpr)   #auc computation

    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC Curve (AUC = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], color='blue', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
