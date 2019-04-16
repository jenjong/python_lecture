# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 06:42:37 2018

@author: Jeon
"""

from scipy import stats
import numpy as np
import sklearn
from sklearn import datasets, linear_model
x = np.random.rand(4,3)
x = np.column_stack( (np.repeat(1,4), x))
#x = np.row_stack( (np.repeat(1,4), x) ) : 
#x = [5.05, 6.75, 3.21, 2.66]
y = np.array([1.65, 26.5, -5.93, 7.96])
y.sum()
regr = linear_model.LinearRegression()
regr.fit(x,y)
regr.predict(x)
regr.coef_
regr.intercept_

regr = linear_model.LinearRegression(fit_intercept = False)
regr.fit(x,y)
regr.predict(x)
regr.coef_
regr.intercept_

import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()