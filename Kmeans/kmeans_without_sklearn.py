import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def kmeans(data, k, iter_time):
    centroids = data[np.random.choice(range(data.shape[0]), k, replace=False)]

    print('centroids test: ', centroids)

    labels = np.zeros(data.shape[0])
    
    for _ in range(iter_time):
        for i in range(data.shape[0]):
            distances = np.linalg.norm(data[i] - centroids, axis=1)
            labels[i] = np.argmin(distances)
        
        for j in range(k):
            centroids[j] = np.mean(data[labels == j], axis=0)
    
    return centroids, labels

#data = pd.read_csv('./k-means/test0.csv')
data = np.genfromtxt('./k-means/test0.csv', delimiter=',', skip_header=True)

print('data shape: ', data.shape)

k = 3

centroids, labels = kmeans(data, k , data.shape[0])

#print(data[:,0])
#print(data[:,1])
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X')
plt.title('K-means testing')
plt.show()
