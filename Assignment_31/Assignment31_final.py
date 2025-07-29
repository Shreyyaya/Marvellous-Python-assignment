import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, roc_auc_score, roc_curve, auc

def main():
    df = pd.read_csv("breast-cancer-wisconsin.csv") 

    df.replace('?', np.nan, inplace=True)

    df.dropna(inplace=True)

    df['CancerType'] = df['CancerType'].replace({2: 0, 4: 1})

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = pd.to_numeric(df[col])  

    x = df.drop('CancerType', axis=1)
    y = df['CancerType']

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    x_train, x_test, y_train , y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=150 , max_depth=10, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print("accuracy is:", accuracy_score(y_test, y_pred)*100)

    dt_clf = DecisionTreeClassifier(max_depth=8)

    importance = pd.Series(model.feature_importances_, index = x.columns)
    importance = importance.sort_values(ascending = False)

    importance.plot(kind = 'bar', figsize=(10,6), title= "Feature importance")
    plt.show()

    voting_clf = VotingClassifier(
        estimators=[
            ('rf', model), 
            ('dt', dt_clf)
            ],
        voting='soft'
    )

    voting_clf.fit(x_train, y_train)

    y_pred = voting_clf.predict(x_test)
    y_prob = voting_clf.predict_proba(x_test)[:, 1]  ##probabilities for positive class


    print(accuracy_score(y_test, y_pred) * 100)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    con_mat = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(con_mat)

    print("ROC AUC Score is:")
    print(roc_auc_score(y_test, y_prob))    #roc auc score

    plt.figure(figsize=(6, 5))
    sns.heatmap(con_mat, annot=True, fmt='d', cmap='Reds', xticklabels=[0, 1], yticklabels=[0, 1])
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
