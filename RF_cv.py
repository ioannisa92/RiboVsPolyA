#! /usr/bin/env python
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, precision_recall_curve,average_precision_score
from sklearn.ensemble import RandomForestClassifier
import pickle

def cross_validate(x, y,folds=10, model=None):

    kfold = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)

    cv_results={}
    cv_results['estimator']=[]
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


        model.fit(x_train, y_train)
        y_proba = model.predict_proba(x_test)[:,1]
        acc = model.score(x_test, y_test)
        precision, recall, _ = precision_recall_curve(y_test, y_proba)
        mean_precision = average_precision_score(y_test, y_proba)
        
        cv_results['estimator'] += [model]
        cv_results['test_acc'] += [acc]
        cv_results['precision'] += [precision]
        cv_results['recall'] += [recall]
        cv_results['average_precision'] += [mean_precision]

    
    return cv_results

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
            best_score=score
            best_estimator=e
    return best_score, best_estimator
    
    
def main():
    ########----------------------Command line arguments--------------------##########
    parser = argparse.ArgumentParser(description="Arguments for RiboVsPoly Classifier")

    parser.add_argument('-X', '--data', default=None, type=str, required=True, help='Classifier input data: expression data')
    parser.add_argument('-Y', '--labels', default=None, type=str, required=True, help='Labels for each sample: Ribo (1), Poly (0)')
    parser.add_argumemnt('-save_best', '--best', action='store_true', required=False, help='whether to save best model. Use with -model_out'
    parser_add_argumnet('-model_out', '--model_file', default='model.sav', type=str, requred=False, help='model filename (full path). Use with -save_best')
    args=parser.parse_args()
    ########----------------------Command line arguments--------------------##########
    
    data = args.data
    labels = args.labels
    save_best = args.best
    model_fn = args.model_file

    classifier_genes = np.loadtxt('../data/ClassifierGenes.txt', dtype='str')

    if '.tsv' in data:
        X = pd.read_csv(data, sep='\t', index_col=0)
        Y = pd.read_csv(labels, sep='\t', index_col=0)
    else:
        raise ValueError('File does not appear to be tab delimited due to erronious extension. Make sure the file is tab delimited')

    X = X.T.loc[classifier_genes].T #making sure genes match dimensionality of trained classifier

    model = RandomForestClassifier(n_estimators=1000, max_depth=5,random_state=42, oob_score=True, n_jobs=-1, verbose=1)
    cv_results = cross_validate(X.values, Y.values, model=model)
    
    cv_mean_precision = np.mean(cv_results['average_precision'])
    print('10-Fold CV average precision: %.3f'%cv_mean_precision)
   
    if save_best:
        best_score, best_estimator = get_best_model(cv_results)
        pickle.dump(best_model, open(model_fn, 'wb'))
      
    np.save('../results/RF_10-foldCV.npy',cv_results)

if __name__ == "__main__":
    main()
