import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

x1, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)

reg = LogisticRegression()
reg.fit(x1, y)

x2, y2 = np.meshgrid(np.linspace(x1[:, 0].min() - 1, x1[:, 0].max() + 1, 100),
                     np.linspace(x1[:, 1].min() - 1, x1[:, 1].max() + 1, 100))
Z = reg.predict(np.c_[x2.ravel(), y2.ravel()])
Z = Z.reshape(x2.shape)

plt.contourf(x2, y2, Z, alpha=0.8)
plt.scatter(x1[:, 0], x1[:, 1], c=y, edgecolors='k')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('testing')
plt.show()