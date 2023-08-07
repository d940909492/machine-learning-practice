import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def linear_regression(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    xy_mean = np.mean(x * y)
    x_sq_mean = np.mean(x ** 2)
    slope = (x_mean * y_mean - xy_mean) / (x_mean ** 2 - x_sq_mean)
    intercept = y_mean - slope * x_mean

    return slope, intercept

def plot_regression(x, y, slope, intercept):
    plt.scatter(x, y, color='blue')
    plt.plot(x, slope * x + intercept, color='red', label='regression line')
    plt.xlabel('age')
    plt.ylabel('salary')
    plt.title('testing')
    plt.legend()
    plt.show()

def main():
    file_path = 'Linear_Regression/test0_1.csv'
    #data = read_csv(file_path)
    data = np.genfromtxt(file_path, delimiter=',', skip_header=True)
    x = data[:, 0]
    y = data[:, 1]

    m , b = linear_regression(x, y)

    plot_regression(x, y, m , b)

if __name__ == "__main__":
    main()
