import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():
    dataset = pd.read_csv("student-mat.csv",  sep=';')

    features = dataset[['G3', 'failures', 'studytime', 'absences']]  #relevant features for clustering

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)  #to scale the features

    model = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)  # setting k=3
    y_kmeans = model.fit_predict(X_scaled)

    dataset['Cluster'] = y_kmeans

    centers_scaled = model.cluster_centers_
    centers_unscaled = scaler.inverse_transform(centers_scaled)  #unscaled cluster centers


    g3_scores = [center[0] for center in centers_unscaled] #cluster interpretation based on g3 score (highest =top)
    sorted_indices = np.argsort(g3_scores)[::-1]  # descending

    cluster_map = {}
    cluster_map[sorted_indices[0]] = "Top Performers"
    cluster_map[sorted_indices[1]] = "Average Students"
    cluster_map[sorted_indices[2]] = "Struggling Students"

    X = features.values  #unscaled for display

    print("Cluster of Top Performers : 0")
    cluster_num = [k for k, v in cluster_map.items() if v == "Top Performers"]
    cluster_num = cluster_num[0]

    count = 0
    for i in range(len(X_scaled)):
        if y_kmeans[i] == cluster_num:
            print(X[i], y_kmeans[i])
            count = count + 1
            if count == 10:
                break         #printing first 10 students

    print("Cluster of Average Students : 1")
    cluster_num = [k for k, v in cluster_map.items() if v == "Average Students"]
    cluster_num = cluster_num[0]

    count = 0
    for i in range(len(X_scaled)):
        if y_kmeans[i] == cluster_num:
            print(X[i], y_kmeans[i])
            count = count + 1
            if count == 10:
                break

    print("Cluster of Struggling Students : 2")
    cluster_num = [k for k, v in cluster_map.items() if v == "Struggling Students"]
    cluster_num = cluster_num[0]

    count = 0
    for i in range(len(X_scaled)):
        if y_kmeans[i] == cluster_num:
            print(X[i], y_kmeans[i])
            count = count + 1
            if count == 10:
                break

if __name__ == "__main__":
    main()
