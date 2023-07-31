import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from training_sources.prepare_for_training import prepare_for_training
import csv

# Linear equation: y = mx+b
# we need Least squares method to find error


"""
def calculate_Error(m, b, np_data):
    totalerror = 0
    for i in range(0, len(np_data)):
        x = np_data[i, 0]
        y = np_data[i, 1]
        totalerror += (y - (m*x + b)) ** 2
    return totalerror / len(np_data)
"""
    
def calculate_error(fdata , obj , m):
    ex_num = fdata.shape[0]
    temp = hyp(fdata, m) - obj
    cost = (1/2)*np.dot(temp.T, temp)/ex_num
    return cost[0][0]

"""
Need predict var and real(actual) var
"""
def grad_dec(num_f, m, learning_rate, learning_times , fdata, obj):
    cost_record = []
    for i in range(learning_times):
        grad_step(m, fdata, learning_rate)
        cost_record.append(calculate_error(fdata, obj, m))
    return cost_record
        
def grad_step(m, fdata, learning_rate):
    num_ex = fdata.shape[0]
    pred = hyp(fdata, m)
    temp_m = m
    temp_m = temp_m - learning_rate * (1/num_ex) * np.dot(pred.T, fdata).T
    m = temp_m

def hyp(fdata, m):
    pred = np.dot(fdata,m)
    return pred

def training(num_f,m, learning_rate, learning_times, fdata, obj):
    error_record = grad_dec(num_f,m, learning_rate, learning_times , fdata, obj)
    return num_f, error_record

## test and run ##
def main():
    fdata = np.np.genfromtxt('test0.csv', delimiter=',')

    sdata = pd.read_csv('test0.csv')

    ### n = int(input('Enter the age: '))

    learning_times = 1000
    learning_rate = 0.001

    num_f = fdata.shape[1]
    m = np.zeros((num_f, 1))

    obj = fdata[: , num_f - 1]

    num_f , error_record = training(num_f,m, learning_rate, learning_times, fdata, obj)   
        
    Sdata = prepare_for_training(fdata,0,0,True)[0]
    
    Error_var = calculate_error(Sdata,obj)
         
    pred = hyp(Sdata,obj)
    
    """
    b = calculate_Error()

    y = m * n + b
    print('predict salary is: ' + str(y))
    """

    x_var = sdata[['age']].values
    y_var = sdata[['salary']].values

    plt.scatter(x_var,y_var,label='data')
    plt.xlabel('age')
    plt.ylabel('salary')
    plt.title('test')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()