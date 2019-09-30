#! /usr/bin/env python
import pandas as pd
import numpy as np
import pickle
import argparse
import sys
import os
'''
Script loads the Random Forest classifer trained to distinguish between polyA and ribo-deplete samples
##INPUT
    -- Tab-delimited file (samples x genes)
##OUTPUT
    -- TSV file containing the following for each sample (samples in rows)
        -- Probability of being Ribo: in turn, probability of being polyA is 1-Ribo
        -- Class assignment of each sample: probability cutoff for now is 0.5: Will likely change in the future
    -- if output tsv filename is not provided, results will be displayed in stdout
'''

def main():
    PATH = os.getcwd()
    
    if len(sys.argv) ==1:
        sys.exit('No input file was passed. Exiting...')
    else:
        expr_input = sys.argv[1]
    
    if len(sys.argv) !=3:
        out = PATH+'out.tsv'
    else:
        out = sys.argv[2]
    
    
    print('reading input...') 
    expr_input = pd.read_csv(expr_input, sep='\t', index_col=0)
    
    model = pickle.load(open(PATH+'/RiboVsPoly.sav', 'rb'))
    print(model)
    
    predictions = model.predict(expr_input)
    predict_proba = model.predict_proba(expr_input)
    

    assert all(predictions)==0
    predictions = pd.DataFrame(np.hstack([predictions.reshape(-1,1), predict_proba]), index=expr_input.index, columns=['Ribo', 'Proba_0', 'Proba_1'])

    predictions.to_csv(out, sep='\t')
    
if __name__ == '__main__':
    main()
