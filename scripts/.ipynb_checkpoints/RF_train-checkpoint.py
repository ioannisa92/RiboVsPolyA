#! /usr/bin/env python

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_recall_curve,average_precision_score

X = pd.read_csv('../data/MergedData_CommonDisease.tsv', sep='\t', index_col=0)
Y = pd.read_csv('../data/MergedLabels_CommonDisease.tsv', sep='\t', index_col=0)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, stratify=Y, random_state=42, test_size=0.3)

model = RandomForestClassifier(n_estimators=5000, max_depth=5,random_state=0, oob_score=True, n_jobs=-1, verbose=1)
model.fit(X_train, Y_train.values.ravel())
pred = model.predict(X_test)
score = (model.score(X_test, Y_test.values.ravel()))

y_proba = model.predict_proba(X_test)[:,1]
precision, recall, _ = precision_recall_curve(Y_test, y_proba)
mean_precision = average_precision_score(Y_test, y_proba)
pred_proba = model.predict_proba(X_test)

print(model.oob_score_)
print(score)
print(mean_precision)
res = {}

res['test_labels'] = Y_test.values.ravel()
res['pred_labels'] = pred
res['pred_proba'] = pred_proba
res['acc'] = score
res['oob_score'] = model.oob_score_
res['model'] = model
res['average_precision'] = mean_precision
res['precision'] = precision
res['recall'] = recall
res['genes'] = X.columns.tolist()
res['importances'] = model.feature_importances_
res['test_samples'] = X_test.index.values

np.save('../results/RF_results_run2.npy', res)
