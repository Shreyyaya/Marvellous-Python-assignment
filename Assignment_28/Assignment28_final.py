import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def MarvellousAdvertise(datapath):

    df = pd.read_csv(datapath)  #get the data

    print("Dataset sample is: ")
    print(df.head())

    print("Clean the dataset")   #cleaning of dataset
    df.drop(columns = ['Unnamed: 0'], inplace = True) 

    print("updated dataset is: ")
    print(df.head())

    print("Missing values in each column", df.isnull().sum())

    print("Statistical summary of dataset is: ")
    print(df.describe())


    print("Correlation matrix is: ")
    print(df.corr())
    plt.figure(figsize= (10,5))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')

    plt.title("Marvellous correlation matrix")
    plt.show()   #plotting the coorelation matrix of features to label

    sns.pairplot(df)
    plt.suptitle("Pairplot of features", y=1.02)
    plt.show()   #pairplot for features

    x = df[['TV', 'radio', 'newspaper']]
    y = df[['sales']]

    x_train, x_test, y_train, y_test = train_test_split(x,y , test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)      #training the dataset using linear regression

    MSE = metrics.mean_squared_error(y_test, y_pred)   #mean squared error
    RMSE = np.sqrt(MSE)                                # root mean squared error
    R2 = metrics.r2_score(y_test, y_pred)              # value of R^2

    print("Mean squared error is: ", MSE)
    print("Root mean squared error is: ", RMSE)
    print("R2 value is: ", R2)

    print("Model coefficient are: ")
    for col, coef in zip(x.columns, model.coef_): 
        print(f"{col}:{coef}")      # displaying value of m

    print("Y intercept is: ", model.intercept_)  # displaying value of c

    plt.figure(figsize= (8,5))
    plt.scatter(y_test, y_pred, color = 'blue')
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.grid(True)
    plt.title("Marvellous advertisement")
    plt.show()            #plotting scatter plot of actual vs predicted sales

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ =="__main__":
    main()    