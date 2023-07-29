import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from Linear_Regression.training_sources import prepare_for_training
import csv

# Linear equation: y = mx+b
# we need Least squares method to find error

def calculate_Error(m, b, np_data):
    totalerror = 0
    for i in range(0, len(np_data)):
        x = np_data[i, 0]
        y = np_data[i, 1]
        totalerror += (y - (m*x + b)) ** 2
    return totalerror / len(np_data)

def calculate_cost(fdata , obj , m):
    ex_num = fdata.shape[0]
    temp = hyp(fdata, m) - obj
    cost = (1/2)*np.dot(temp.T, temp)/ex_num
    return cost[0][0]

"""
Need predict var and real(actual) var
"""
def grad_dec(num_f, m, learning_rate, learning_times , fdata):
    for i in range(learning_times):
        grad_step(m, fdata, learning_rate)
    return
        
def grad_step(m, fdata, learning_rate):
    num_ex = fdata.shape[0]
    pred = hyp(fdata, m)
    temp_m = m
    temp_m = temp_m - learning_rate * (1/num_ex) * np.dot(pred.T, fdata).T
    m = temp_m
    return

def hyp(fdata, m):
    pred = np.dot(fdata,m)
    return pred


## test and run ##
def main():
    fdata = np.genfromtxt('test0.csv', delimiter=',')

    n = int(input('Enter the age: '))
    learning_times = 1000
    learning_rate = 0.001

    num_f = fdata.shape[1]
    m = np.zeros((num_f, 1))

    obj = fdata[: , num_f - 1]

    grad_dec(num_f,m, learning_rate, learning_times , fdata)

    b = calculate_Error()

    y = m * n + b
    print('predict salary is: ' + str(y))

if __name__ == '__main__':
    main()