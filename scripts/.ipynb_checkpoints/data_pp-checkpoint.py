#! /usr/bin/env python

import pandas as pd
import numpy as np
from scipy.sparse import issparse
import matplotlib.pyplot as plt


    
def ensembl_to_hugo( df):

    conversion_file='../data/EnsGeneID_Hugo_Observed_Conversions.txt'

    gene_length=dict()
    ensemble_to_hugo_dct=dict()
    with open(conversion_file, 'r') as f:
        lines=f.readlines()
        for line in lines[1:]:
            line=line.split()
            length=float(line[2])/1000 # numbers in kilobases
            hugo=line[0]
            ensemble=line[1]
            gene_length[ensemble]=length
            ensemble_to_hugo_dct[ensemble]=hugo

    # df needs to be cells by genes
    # genes need to be in ensembl space

    df=df.T #genes by cells
    ensemble_genes=df.index #ensembl ids from df
    hugo_genes=[]
    nan_count=0
    for ensembl in ensemble_genes:
        try:
            hugo=ensemble_to_hugo_dct[ensembl]
            hugo_genes+=[hugo]
        except KeyError:
            nan_count+=1
            hugo_genes+=[np.nan]
    
    nan_bool=(np.array(hugo_genes)!='nan')
    gene_renaming_dict=dict(zip(ensemble_genes, hugo_genes))
    df=df.rename(index=gene_renaming_dict)#nans included
    df=df[nan_bool] #nans excluded
    df=df.T #cells by genes

    return df
