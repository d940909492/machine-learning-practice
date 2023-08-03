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

class linear_regression:
    def __init__(self,data,obj,learning_times,learning_rate, polynomial_degree=0, sinusoid_degree=0, normalize_data=True):
        
        data_, x_mean, x_deviation = prepare_for_training(data, polynomial_degree, sinusoid_degree, normalize_data)

        self.data = data_
        self.learning_times = learning_times
        self.learning_rate = learning_rate

        self.x_mean = x_mean
        self.x_deviation = x_deviation

        self.polynomial_degree = polynomial_degree
        self.sinusoid_degree = sinusoid_degree
        self.normalize_data = normalize_data

        num_f = data.shape[1]
        self.m = np.zeros((num_f, 1))
        self.obj = obj

    """
    Need predict var and real(actual) var
    """
    def grad_dec(self , learning_rate, learning_times):
        cost_record = []
        num_ex = self.obj.shape[0]
        for i in range(learning_times):
            self.grad_step(learning_rate)
            cost_record.append(self.calculate_error(self.data,self.obj))
        return cost_record


    def grad_step(self,  learning_rate):
        num_ex = self.data.shape[0]
        pred = linear_regression.hyp(self.data, self.m)
        temp_m = m
        temp_m = temp_m - learning_rate * (1/num_ex) * np.dot(pred.T, self.data).T
        m = temp_m


    def hyp(data, m):
        pred = np.dot(data,m)
        return pred

    def training(self, learning_rate, learning_times):
        error_record = self.grad_dec(learning_rate,learning_times)
        return self.m, error_record

    def calculate_error(fdata , obj , m):
        ex_num = fdata.shape[0]
        temp = linear_regression.hyp(fdata, m) - obj
        cost = (1/2)*np.dot(temp.T, temp)/ex_num
        return cost[0][0]
    
    def get_error(self, data, obj):

        data_, _, _ = prepare_for_training(data, self.polynomial_degree, self.sinusoid_degree, self.normalize_data)
        return self.cost_function(data_, obj)

    def predict(self, data):
        data_, _, _ = prepare_for_training(data, self.polynomial_degree, self.sinusoid_degree, self.normalize_data)
        return self.hypothesis(data_)


    ## test and run ##

    """
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
    """