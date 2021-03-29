#!/usr/bin/env python
# coding: utf-8

# # The following notebook merges generates a linear classifier based on RiboD and PolyA datasets
# * To be run after setup.sh

## Import libraries

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

import pickle

## Import Data
X = pd.read_csv('../data/MergedData_Balanced.tsv', sep='\t', index_col=0)
Y = pd.read_csv('../data/MergedLabels_Balanced.tsv', sep='\t', index_col=0)

## Train and Test Linear Regression Model
# Create test and train data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, stratify=Y, random_state=42, test_size=0.3)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train regression model
regr.fit(X_train, Y_train)
regr.score(X_train, Y_train)

# Apply Linear Regression model to test data
pred = regr.predict(X_test)

# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(Y_test, pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(Y_test, pred))

## Save Linear Regression Model
filename = "../models/linear_regression_model.sav"
pickle.dump(regr, open(filename,"wb"))
