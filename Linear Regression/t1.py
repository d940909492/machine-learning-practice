import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Linear equation: y = mx+b

def calculate_Error(m, b, np_data):
    totalerror = 0
    for i in range(0, len(np_data)):
        x = np_data[i, 0]
        y = np_data[i, 1]
        totalerror += (y - (m*x + b)) ** 2
    return totalerror / len(np_data)

def main():
    b = 0
    m = 0
    n = int(input('Enter the age: '))
    error_point = calculate_Error()

    y = m * n + error_point
    print('predict salary is: ' + str(y))

if __name__ == '__main__':
    main()