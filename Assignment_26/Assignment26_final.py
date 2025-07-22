import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def PlayPredictorLogistic(Datapath):
    df = pd.read_csv(Datapath)
    print("Dataset loaded successfully")
    print(df.head())

    df.drop(columns=['Unnamed: 0'], inplace=True)  #dropping unwanted columns

    
    df['Play'] = df['Play'].map({'No': 0, 'Yes': 1})  #label encoding

    df_encoded = pd.get_dummies(df, columns=df.select_dtypes(include=['object']).columns, drop_first=True)
    #used get_dummies method to perfrom one hot encoding as logistic regression doesnt work with string values

    print("Encoded data using get_dummies:")
    print(df_encoded.head())    #encoded features data 

    x = df_encoded.drop(columns=['Play'])
    y = df_encoded['Play']

    print("Dimensions of target:", x.shape)
    print("Dimensions of labels:", y.shape)

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    con_mat = confusion_matrix(y_test, y_pred)

    print("Accuracy is:", accuracy * 100)
    print("Confusion matrix:")
    print(con_mat)


def main():
    PlayPredictorLogistic("PlayPredictor.csv")

if __name__ == "__main__":
    main()
