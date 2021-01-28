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

def gene_checker(input_file):
    '''
    Function checks the input file's genes.
    The intersection between the input file's genes and the predetermined classifier genes is taken.
    Then the function checks for genes are not present in the input file.
    For those genes, the expression vector is set to 0.
    A new dataframe is returned with the correct order of genes.

    Parameters
    ----------
    input_file; pandas df - shape should be (samples x genes)
    
    Returns
    ---------
    new_input_file; pandas df - shape (samples x genes)
    '''
    
    classifier_genes = np.loadtxt('./data_test/ClassifierGenes.txt', dtype='str')
    classifier_genes_meanexpr = np.load('./data_test/ClassifierGenes_MeanExpr.npy', allow_pickle=True).item()
    common_genes = set(classifier_genes).intersection(input_file.columns)
    uncommon_genes = set(classifier_genes).difference(input_file.columns)
    #new_input_file = input_file.T.loc[classifier_genes].T # seleting classifier selected genes in the classifier determined order
    print(len(common_genes ))
    for gene in uncommon_genes:
        input_file[gene] = [classifier_genes_meanexpr[gene]]*input_file.shape[0]

    new_input_file = input_file.T.loc[classifier_genes].T

    # will fill genes that do not exist in the input with zero
    # if no NAN values, none will be filled
    new_input_file = new_input_file.fillna(0) 
    
    return new_input_file
     
def main():
    #PATH = os.getcwd()

    ########----------------------Command line arguments--------------------##########
    parser = argparse.ArgumentParser(description="Arguments for preranked an single sample GSEA")

    parser.add_argument('-i', '--input', default=None, type=str, required=True, help='Input expression file (samples x genes')
    parser.add_argument('-model', '--MODEL', type=str, required=False, default='./models/RiboVsPoly_balanced_max_depth_2.sav', help='Path to saved model')
    parser.add_argument('-o', '--output', default='out.tsv', type=str, required=False, help='TSV Output prediction file')
    args=parser.parse_args()

    ########----------------------Command line arguments--------------------##########

    expr_input = args.input
    out = args.output
    model = args.MODEL

    print('reading input...') 
    expr_input = pd.read_csv(expr_input, sep='\t', index_col=0)

    print("before gene intersection...")
    print(expr_input.shape)
    expr_input = gene_checker(expr_input) # making sure genes are correct for classifier
    print("After gene intersection...")
    print(expr_input.shape)

    print('applying model...')
    model = pickle.load(open(model, 'rb'))
    print(model)
    
    predictions = model.predict(expr_input)
    predict_proba = model.predict_proba(expr_input)
    
    print("saving results...")
    predictions = pd.DataFrame(np.hstack([predictions.reshape(-1,1), predict_proba]), index=expr_input.index, columns=['Ribo', 'Proba_0', 'Proba_1'])

    predictions.to_csv(out, sep='\t')
    
if __name__ == '__main__':
    main()
