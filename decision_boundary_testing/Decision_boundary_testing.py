import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('./decision_boundary/bank.csv', delimiter=';')

# Convert 'housing' column to numerical values
label_encoder = LabelEncoder()
data['housing'] = label_encoder.fit_transform(data['housing'])

x = data[['age', 'balance']].values
y = data['housing'].values

model = LogisticRegression()
model.fit(x, y)

x1_range = np.linspace(min(x[:, 0]), max(x[:, 0]), 400)
x2_range = np.linspace(min(x[:, 1]), max(x[:, 1]), 400)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)
x_grid = np.c_[x1_grid.ravel(), x2_grid.ravel()]

y_grid = model.predict(x_grid)
y_grid = y_grid.reshape(x1_grid.shape)

plt.contourf(x1_grid, x2_grid, y_grid, cmap=plt.cm.Spectral, alpha=0.8)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Spectral)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Decision Boundary')
plt.show()
