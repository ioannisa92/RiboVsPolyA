#!/usr/bin/env python
# coding: utf-8

# # The following notebook generates a logistic classifier based on RiboD and PolyA datasets
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
X = pd.read_csv('../data/treehouse_SRP_data/merged_SRP_data.tsv', sep='\t', index_col=0)
Y = pd.read_csv('../data/treehouse_SRP_data/merged_SRP_labels.tsv', sep='\t', index_col=0)

## Train and Test Logistic Regression Model
# Create test and train data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, stratify=Y, random_state=42, test_size=0.3)

# Create logistic regression object
# Increase max_iter from 100 to 1000 to allow model to converge
regr = linear_model.LogisticRegression(max_iter=1000)

# Train regression model
regr.fit(X_train, Y_train)
regr.score(X_train, Y_train)

# Apply logistic regression model to test data
pred = regr.predict(X_test)

# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(Y_test, pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(Y_test, pred))

## Save logistic regression Model
filename = "../models/SRP_logistic_regression_model.sav"
pickle.dump(regr, open(filename,"wb"))
