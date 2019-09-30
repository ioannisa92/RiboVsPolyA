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

    ########----------------------Command line arguments--------------------##########
    parser = argparse.ArgumentParser(description="Arguments for preranked an single sample GSEA")

    parser.add_argument('-i', '--input', default=None, type=str, required=True, help='Inpy expression file (samples x genes')
    parser.add_argument('-o', '--output', default='out.tsv', type=str, required=False, help='Output prediction file')
    args=parser.parse_args()

    ########----------------------Command line arguments--------------------##########

    expr_input = args.input
    out = args.output
    
    print('reading input...') 
    expr_input = pd.read_csv(expr_input, sep='\t', index_col=0, nrows=20)
    
    model = pickle.load(open(PATH+'/RiboVsPoly.sav', 'rb'))
    print(model)
    
    predictions = model.predict(expr_input)
    predict_proba = model.predict_proba(expr_input)
    

    predictions = pd.DataFrame(np.hstack([predictions.reshape(-1,1), predict_proba]), index=expr_input.index, columns=['Ribo', 'Proba_0', 'Proba_1'])

    predictions.to_csv(out, sep='\t')
    
if __name__ == '__main__':
    main()
