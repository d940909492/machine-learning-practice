import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./stat_testing/test.csv", header=None, names=["v"])

plt.plot(data["v"], [0] * len(data), "o", markersize=10, color="blue")
plt.yticks([])
plt.xlabel("v")
plt.tight_layout()

plt.show()
