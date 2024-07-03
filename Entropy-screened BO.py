#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel, Matern, ConstantKernel, ExpSineSquared, RBF, RationalQuadratic
from itertools import product
from scipy.optimize import minimize
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
from sklearn.model_selection import cross_validate as CV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from scipy.stats import norm
import random
import time
import math


# In[ ]:


# Load the spreadsheet
file_path = 'Entropy-screened BO dataset.csv'
data = pd.read_csv(file_path)
# Display the first few rows of the dataframe to understand its structure
data.head()


# In[ ]:


# Renaming columns for clarity
data.columns = ['Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Mo', 'Objective']

# Splitting the data into inputs (X) and output (y)
X = data[['Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Mo']].values
y = data['Objective'].values
X = X/90


# In[ ]:


#fitting
kernel = 1.0 * Matern(nu=1.5) 
gp = GaussianProcessRegressor(kernel=kernel, alpha = 0.15, n_restarts_optimizer=1000, normalize_y = True)
gp.fit(X, y)
gp.kernel_


# In[ ]:


def generate_constrained_points(variable_index, n_points):
    x_points = np.linspace(0, 1, n_points)
    points = np.zeros((n_points, 6))

    for i in range(n_points):
        x = x_points[i]
        points[i, variable_index] = x

        candidates = []
        random_numbers = [random.randint(1, n_points) for _ in range(5)]
        total = sum(random_numbers)
        results = [round((1-x)*number / total, 4) for number in random_numbers] #randomly generate 6 numbers with boundary
        candidates.append(results)
        # # allocate array
        selected_candidate = candidates[0]
        
        candidate_index = 0
        for j in range(6):
            if j != variable_index:
                points[i, j] = selected_candidate[candidate_index]
                candidate_index += 1
                
    return points


# In[ ]:


def average_predictions(gp, variable_index, n_points, n_iterations=10000):
    total_y_pred = 0
    total_sigma = 0
    pointsarray = []
    for _ in range(n_iterations):
        points = generate_constrained_points(variable_index, n_points)
        pointsarray.append(points)
        y_pred, sigma = gp.predict(points, return_std=True)

        total_y_pred += y_pred
        total_sigma += sigma

    # calculation of average
    average_y_pred = total_y_pred / n_iterations
    average_sigma = total_sigma / n_iterations
    
    for i in range(n_iterations-1):
    # concatenate pointsarray[i] to result_array
        result_array = np.concatenate((pointsarray[i], pointsarray[i+1]), axis=0)

    return average_y_pred, average_sigma, result_array


# In[ ]:


def find_uncertainty_by_line(gp, n_points):
    variable_index=[0,1,2,3,4,5]
    y_pred_list=[]
    sigma_list=[]
    array_list=[]
    for i in range(len(variable_index)):
        y_pred, sigma, array = average_predictions(gp, variable_index[i], n_points)
        y_pred_list.append(y_pred)
        sigma_list.append(sigma)
        array_list.append(array)
    return y_pred_list, sigma_list, array_list


# In[ ]:


n_points = 91  # number of points to generate

start_time = time.time()  # check time

y_pred, sigma, array = find_uncertainty_by_line(gp, n_points)

end_time = time.time()
total = end_time - start_time
print("prediction time :", total) 


# In[ ]:


# Plotting
variable = [0,1,2,3,4,5]
variable_index = 5
plt.figure(figsize=(6, 4.5))
plt.plot(array[variable_index][:n_points, variable[variable_index]], y_pred[variable_index],'b-',label = 'GP prediction')
plt.fill_between(array[variable_index][:n_points, variable[variable_index]], y_pred[variable_index] - sigma[variable_index], y_pred[variable_index] + sigma[variable_index], alpha=0.2, color='blue', label = 'Uncertainty')
plt.xlabel(f'{data.columns[variable[variable_index]]}')
plt.ylabel('OWS overpotential(mV)')
plt.xlim(0,0.9)
plt.ylim(250,900)
plt.legend(loc='upper left')
plt.show()


# In[ ]:


def acquisition_func(gp, n_points):
    x_points = np.linspace(0, 90, n_points)
    points = np.zeros((n_points, 6))

    candidates = []
    y_pred_list = []
    sigma_list = []
    entropy = []
    for i in range(1000000):
        random_numbers = [random.randint(1, 100) for _ in range(6)]
        # calculate the sum of six random numbers
        total = sum(random_numbers)
        # calculate the normalized value and round it to 2 decimals
        results = [round(0.9*number / total, 2) for number in random_numbers]
        candidates.append(results)
    
    y_pred, sigma = gp.predict(candidates, return_std=True)
    for i in range(len(candidates)):
        s = (-1)*0.1*np.log(0.05)
        for j in range(6):
            s += (-1)*(candidates[i][j]*np.log(candidates[i][j]+1e-9))
        entropy.append(s)
    return y_pred, sigma, entropy, candidates


# In[ ]:


acq_y_pred, sigma, entropy, candidates = acquisition_func(gp, 91)
acq_array = acq_y_pred.max() - acq_y_pred + entropy*sigma
candidates_list = []


# In[ ]:


for i in range(99):
    max_acq_index = np.argmax(acq_array)
    candidates_list.append(candidates[max_acq_index])
    acq_array = np.delete(acq_array, max_acq_index, axis=0)
print(candidates_list)

