#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 2020. 
Summary of the file:

Lets print out the slopes.
    - use numpy
    
Then run linear regression with scikit learn:
    - prepare 2012 data
    - fit
    - plot
    - find error
    
    - prepare 1975 data
    - fit
    - plot
    - find error
    #i should update test/train split 
"""
###Linear regression - summary

#find slopes
old_slope_1975, old_intercept_1975 = np.polyfit(length_1975, depth_1975, 1)
new_slope_2012, new_intercept_2012 = np.polyfit(length_2012, depth_2012, 1)

print('1975: slope of length to depth =', old_slope_1975)
print('1975: intercept of length to depth =', old_intercept_1975)
print('2012: slope of length to depth =', new_slope_2012)
print('2012: intercept of length to depth =', new_intercept_2012)

#linear regression with sklearn
from sklearn.linear_model import LinearRegression

#prep data for 1975
x = length_1975
y = depth_1975 
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
regressor = LinearRegression()
regressor.fit(x, y)
y_pred = regressor.predict(x)
#plot the model
plt.figure()
plt.scatter(x, y, color = 'orange')
plt.plot(x, y_pred, color = 'blue')
plt.title('Length versus Depth of beak in 1975')
plt.xlabel('Length')
plt.ylabel('Depth')
plt.show()
#finding error
msqe = sum((y_pred - y) * (y_pred - y)) / y.shape[0]
rmse = np.sqrt(msqe)

#prep data for 2012
x = length_2012
y = depth_2012 
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
regressor = LinearRegression()
regressor.fit(x, y)
y_pred = regressor.predict(x)
#plot
plt.figure()
plt.scatter(x, y, color = 'blue')
plt.plot(x, y_pred, color = 'black')
plt.title('Length versus Depth of beak in 2012')
plt.xlabel('Length')
plt.ylabel('Depth')
plt.show()
#finding error
msqe = sum((y_pred - y) * (y_pred - y)) / y.shape[0]
rmse = np.sqrt(msqe)
