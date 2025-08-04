import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    # Loading and cleaning data
    df = pd.read_csv("Combined_News.csv")
    df.dropna(inplace=True)

    useful_columns = ['title', 'text', 'subject', 'label']
    df = df[useful_columns]

    label_encoder = LabelEncoder()
    df['label'] = label_encoder.fit_transform(df['label'])

    df['content'] = df['title'] + " " + df['text']


    tf_idf = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = tf_idf.fit_transform(df['content'])  
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    
    log_clf = LogisticRegression(max_iter=1000)
    dt_clf = DecisionTreeClassifier(random_state=42)

    log_clf.fit(X_train, y_train)
    dt_clf.fit(X_train, y_train)

    # Predictions
    y_pred_log = log_clf.predict(X_test)
    y_pred_dt = dt_clf.predict(X_test)

    # Hard Voting
    voting_hard = VotingClassifier(
        estimators=[
            ('lr', log_clf), 
            ('dt', dt_clf)
            ], 
            voting='hard')
    voting_hard.fit(X_train, y_train)
    y_pred_hard = voting_hard.predict(X_test)

    # Soft Voting
    voting_soft = VotingClassifier(
        estimators=[
            ('lr', log_clf), 
            ('dt', dt_clf)
            ],
            voting='soft')
    voting_soft.fit(X_train, y_train)
    y_pred_soft = voting_soft.predict(X_test)

    models = {
        "Logistic Regression": y_pred_log,    #making a dictionary name models which contains the models used in voting classifiers
        "Decision Tree": y_pred_dt,
        "hard Voting": y_pred_hard,
        "soft Voting ": y_pred_soft
    }

    for name, pred in models.items():           #name refers to algo name, pred is the y_pred value
        print(f"\n-----{name} ------")
        print("Accuracy:", round(accuracy_score(y_test, pred)))
        print("Classification Report:")
        print(classification_report(y_test, pred))
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, pred))

if __name__ == "__main__":
    main()
