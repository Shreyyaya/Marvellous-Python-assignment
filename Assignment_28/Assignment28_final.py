import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix  

def WinePredictor(Datapath):
    df = pd.read_csv(Datapath)  #get the data

    df.dropna(inplace = True)  #drop null values

    x = df.drop(columns = ['Class'])  #training of model
    y = df['Class']

    scaler = StandardScaler()  #scaling to train model
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size= 0.2, random_state=42)    

    accuracy_scores =[]
    k_range = range(1,21)

    for i in k_range:
        model = KNeighborsClassifier(n_neighbors= i)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(accuracy)                 #loop to display the accuracy scores for values of k ranging between 1 to 20

    plt.figure(figsize = (8,5))
    plt.plot(k_range, accuracy_scores, marker = 'o', linestyle = '--')
    plt.title("Accuracy vas k values")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy scores")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()             #plotting of accuracy scores varying according to the K values


    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]  
    print("Best value of K is: ", best_k)     #displaying the best k value which gives max accuracy

    model = KNeighborsClassifier(n_neighbors= i)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)         #training of model using k nearest neighbour algorithm

    print("Final best accuracy is: ", accuracy*100)

    con_mat = confusion_matrix(y_test, y_pred)
    print(con_mat)        #confusion matrix


def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()    