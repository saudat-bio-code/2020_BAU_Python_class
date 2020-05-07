#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29
"""
#random forest regression for 2012 data
x = length_2012 
y = depth_2012
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(x, y)
y_pred = regressor.predict(x)
#sort x
s_x = np.sort(x, axis = None).reshape(-1, 1)
#plot
plt.figure()
x_grid = np.arange(min(s_x), max(s_x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'blue')
plt.plot(x_grid, regressor.predict(x_grid), color = 'black')
plt.title('Length versus Depth of beak in 2012')
plt.xlabel('Length')
plt.ylabel('Depth')
plt.show()
#finding error
msqe = sum((y_pred - y) * (y_pred - y)) / y.shape[0]
rmse = np.sqrt(msqe)


#random forest for 1975
x = length_1975 
y = depth_1975
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(x, y)
y_pred = regressor.predict(x)
#sort and grid
s_x = np.sort(x, axis = None).reshape(-1, 1)
plt.figure()
x_grid = np.arange(min(s_x), max(s_x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'orange')
plt.plot(x_grid, regressor.predict(x_grid), color = 'red')
plt.title('Length versus Depth of beak in 1975')
plt.xlabel('Length')
plt.ylabel('Depth')
plt.show()
#lets find error
msqe = sum((y_pred - y) * (y_pred - y)) / y.shape[0]
rmse = np.sqrt(msqe)
