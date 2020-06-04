#! /usr/bin/env python
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.metrics import f1_score, precision_recall_curve,average_precision_score
from sklearn.ensemble import RandomForestClassifier
import pickle

def cross_validate(x, y,folds=10, model=None):

    kfold = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)

    cv_results={}
    cv_results['estimators']=[]
    cv_results['test_acc']=[]
    cv_results['precision']=[]
    cv_results['recall']=[]
    cv_results['average_precision']=[]
    print('cross validating...')
    
    for train_idx, test_idx in kfold.split(x, y):

        x_train = x[train_idx]
        y_train = y[train_idx]
        x_test = x[test_idx]
        y_test = y[test_idx]


        model.fit(x_train, y_train.flatten())
        y_proba = model.predict_proba(x_test)[:,1]
        acc = model.score(x_test, y_test)
        precision, recall, _ = precision_recall_curve(y_test, y_proba)
        mean_precision = average_precision_score(y_test, y_proba)
        
        cv_results['estimators'] += [model]
        cv_results['test_acc'] += [acc]
        cv_results['precision'] += [precision]
        cv_results['recall'] += [recall]
        cv_results['average_precision'] += [mean_precision]

    
    return cv_results

def gscv(X,Y, model, parameters, folds=10, jobs=1):
    clf = GridSearchCV(model, parameters, cv=folds, n_jobs=jobs)
    print("grid searching...")
    clf.fit(X, Y.values.ravel())
    results = clf.cv_results_
    best_model = clf.best_estimator_
    best_params = clf.best_params_
    
    return results, best_model, best_params

def get_best_model(cv_results):
    '''
    Function takes in results from function cross_validate and finds the nest estimator
    If multiple estimators have achieved the same precision, then a random one is selected
    '''
    best_score=None
    best_estimator=None
    for i,e in enumerate(cv_results['estimators']):
        score = cv_results['precision']
        
        if best_score is None or score>best_score:
            best_score = score
            best_estimator = e
    return best_score, best_estimator
    
    
def cv_main(X, Y):

    model = RandomForestClassifier(n_estimators=1000, max_depth=5,random_state=42, oob_score=True, n_jobs=-1, verbose=1)
    cv_results = cross_validate(X.values, Y.values, model=model)
    
    cv_mean_precision = np.mean(cv_results['average_precision'])
    print('10-Fold CV average precision: %.3f'%cv_mean_precision)
   
    best_score, best_estimator = get_best_model(cv_results)
    return best_score, cv_results, best_estimator
    

if __name__ == "__main__":
    ########----------------------Command line arguments--------------------##########
    parser = argparse.ArgumentParser(description="Arguments for RiboVsPoly Classifier")

    parser.add_argument('-X', '--data', default=None, type=str, required=True, help='Classifier input data: expression data')
    parser.add_argument('-Y', '--labels', default=None, type=str, required=True, help='Labels for each sample: Ribo (1), Poly (0)')
    parser.add_argument('-cv', '--CV', action='store_true', required=False, help='whether to perform cross validation')
    parser.add_argument('-grid_search', '--GRIDCV', action='store_true', required=False, help='whether to perform parameter selection')
    parser.add_argument('-model_out', '--model_file', default='model.sav', type=str, required=False, help='model filename (full path). Use with -save_best')
    parser.add_argument('-results_out', '--results_file', default='model.sav', type=str, required=False, help='resukts filename (full path)')
    args=parser.parse_args()
    ########----------------------Command line arguments--------------------##########

    data = args.data
    labels = args.labels
    model_fn = args.model_file
    cv = args.CV
    grid_search = args.GRIDCV
    results_out = args.results_file

    if '.tsv' in data:
        X = pd.read_csv(data, sep='\t', index_col=0)
        Y = pd.read_csv(labels, sep='\t', index_col=0)
    else:
        raise ValueError('File does not appear to be tab delimited due to erronious extension. Make sure the file is tab delimited')
    

    if cv:
        best_score, cv_results, best_estimator  = cv_main(X, Y, save_best=save_best)
        pickle.dump(best_estimator, open(model_fn, 'wb'))
        np.save('../results/RF_10-foldCV.npy',cv_results)

    if grid_search:
        model=RandomForestClassifier()
        param_grid={'n_estimators':np.arange(100,2000,100), 'max_depth': np.arange(1,10,1), "min_samples_leaf":np.arange(1,10,1),"min_samples_split":np.arange(2,20,2)}
        results, best_model, best_params = gscv(X,Y, model, parameters=param_grid, jobs=13)
        print("saving best model...")
        pickle.dump(best_model, open(model_fn, 'wb'))
        print("saving resutls...")
        np.save(results_out,results)
        print(best_params)

        # unbalanced best params 
        #RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
        #                       criterion='gini', max_depth=1, max_features='auto',
        #                       max_leaf_nodes=None, max_samples=None,
        #                       min_impurity_decrease=0.0, min_impurity_split=None,
        #                       min_samples_leaf=3, min_samples_split=2,
        #                       min_weight_fraction_leaf=0.0, n_estimators=700,
        #                       n_jobs=None, oob_score=False, random_state=None,
        #                       verbose=0, warm_start=False)


        #balanced best params
        #RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
        #                       criterion='gini', max_depth=7, max_features='auto',
        #                       max_leaf_nodes=None, max_samples=None,
        #                       min_impurity_decrease=0.0, min_impurity_split=None,
        #                       min_samples_leaf=1, min_samples_split=2,
        #                       min_weight_fraction_leaf=0.0, n_estimators=500,
        #                       n_jobs=None, oob_score=False, random_state=None,
        #                       verbose=0, warm_start=False)
