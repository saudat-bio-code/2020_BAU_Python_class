import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


""" Need to pass the dataset parameter which is 'SEN4018_Combined.csv'
    You can use:          dataset = pd.read_csv('SEN4018_Combined.csv')
"""
def linearRegression(dataset):
    x = dataset.iloc[:, 3].values # Square meter (net)
    y = dataset.iloc[:, 1].values # Price

    # Create training and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)
    x_train = x_train.reshape(-1, 1)
    x_test = x_test.reshape(-1, 1)
    y_train = y_train.reshape(-1, 1)


    # Train the model using the training set
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    # Predict the test results
    y_pred = regressor.predict(x_test)

    # Visulize the training set results
    plt.scatter(x_train, y_train, color = 'red')
    plt.plot(x_train, regressor.predict(x_train), color = 'blue')
    plt.title('Price vs Square Meter (Net) - Training set')
    plt.xlabel('Square Meter (Net)')
    plt.ylabel('Price')
    plt.show()

    # Visulize the test set results
    plt.scatter(x_test, y_test, color = 'red')
    plt.plot(x_test, regressor.predict(x_test), color = 'blue')
    plt.title('Price vs Square Meter (Net) - Test set')
    plt.xlabel('Square Meter (Net)')
    plt.ylabel('Price')
    plt.show()

    coef = regressor.coef_[0][0]
    intercept = regressor.intercept_[0]
    print("Linear Regression Equation is:\tPrice = (", coef, " * Square Meter ) + (", intercept, ")")

    userSquareMeter = int(input("Enter a square meter value to predict a price using Simple Linear Regression: "))
    print("Square Meter: ", userSquareMeter, " m^2")
    print("Predicted Price: ", regressor.predict([[userSquareMeter]])[0][0], " TL")

ds = pd.read_csv('SEN4018_Combined.csv')

# Predict prices according to net areas of houses in square meter
linearRegression(ds)