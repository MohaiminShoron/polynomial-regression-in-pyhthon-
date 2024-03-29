# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:41:51 2019

@author: Shoron
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
'''
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
'''

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#fitting linear regression to the data set
from sklearn.linear_model import LinearRegression
lin_reg= LinearRegression()
lin_reg.fit(X,y)

#fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)
lin_reg2=LinearRegression()
lin_reg2.fit(X_poly,y)

#visualizing the linear regression results

plt.scatter(X,y)
plt.plot(X,lin_reg.predict(X))
plt.title('Truth or bluff(linear regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()


#visualizing the polynomial regression results
x_grid=np.arange(min(X),max(X),0.1)
x_grid=x_grid.reshape(len(x_grid),1)
plt.scatter(X,y,color='red')
plt.plot(x_grid,lin_reg2.predict(poly_reg.fit_transform(x_grid)),color='blue')
plt.title('Truth or bluff(polynomial regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

#predicting a new result with linear regression
lin_reg.predict([[6.5]])
#predicting a new result with polynomial regression
lin_reg2.predict(poly_reg.fit_transform([[6.5]]))