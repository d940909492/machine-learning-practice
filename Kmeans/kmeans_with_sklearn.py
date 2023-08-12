import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('./k-means/test0.csv')

features = data[['age', 'salary']]

x = features.to_numpy()

n = 3

kmeans = KMeans(n_clusters=n)
kmeans.fit(x)
label = kmeans.labels_
center = kmeans.cluster_centers_

plt.scatter(x[:, 0], x[:, 1], c=label)
plt.scatter(center[:, 0], center[:, 1], marker='D', s=200, c='black')
plt.xlabel('age')
plt.ylabel('salary')
plt.title('k means testing')
plt.show()
