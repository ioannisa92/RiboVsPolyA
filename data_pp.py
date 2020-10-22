#! /usr/bin/env python

import pandas as pd
import numpy as np
from scipy.sparse import issparse
import matplotlib.pyplot as plt
#from keras_deep_graph_learning.examples.utils import *
def gene_intersection(dfs=None):
    # list of dfs needs to samples by genes
    # dfs is a list of dataframes

    # function returns the same list of dataframes with genes intersected for all three

    if len(dfs) <2:
        print('cannot do intersection with less than 2 dataframes')
        sys.exit(0)

    all_genes=[]
    for df in dfs:
        all_genes+=[df.columns]

    intersection_genes=set.intersection(*map(set,all_genes))

    #print('%d genes intersect'%len(intersection_genes))

    intersected_dfs=[]
    for df in dfs:

        intersected_df=df[list(intersection_genes)]
        intersected_dfs+=[intersected_df]

        #print('shape after gene intersection:')
        #print(intersected_df.shape)

    return intersected_dfs

def remove_allzero(df,ax=0):
    '''
    removes all zero entries on the axis selected
    ax =1 means samples because the .sum function sums columns here
    ax =0 means genes because the .sum function in numpy sums rows
    '''
    if isinstance(df, pd.DataFrame):
        X = df.values
    else:
        X = df

    bool = (X.sum(axis=ax)!=0)
    return df.T[bool].T

def sample_intersection(dfs=None):
    # list of dfs needs to samples by genes
    # dfs is a list of dataframes

    # function returns the same list of dataframes with genes intersected for all three

    if len(dfs) <2:
        print('cannot do intersection with less than 2 dataframes')
        sys.exit(0)

    all_genes=[]
    for df in dfs:
        all_genes+=[df.index]

    intersection_samples=set.intersection(*map(set,all_genes))

    #print('%d samples intersect'%len(intersection_samples))

    intersected_dfs=[]
    for df in dfs:

        intersected_df=df.loc[list(intersection_samples)]
        intersected_df = intersected_df[~intersected_df.index.duplicated(keep='first')] #removing potential duplicate indices
        intersected_dfs+=[intersected_df]

        #print('shape after sample intersection:')
        #print(intersected_df.shape)

    return intersected_dfs

def high_variance(x,k=10000, inplace=False):
    '''
    function selectes top k most variant genes in X

    X should be samples x genes

    returns indeces of top k genes in X
    if inplace is selected, the x will be subsetted for the most variable genes
    else the indeces of the most variable genes are returned
    '''

    if isinstance(x, pd.DataFrame):
        X = x.values
    if issparse(x):
        X = x.todense()
    else:
        X = x


    var = X.var(axis=0) #gets variance of each gene
    var = np.argsort(var)[::-1] #sorts genes be variance
    topk_genes = var[:k] # top k most variable gene

    #if topk_genes.ndim !=1:
    topk_genes = np.array(topk_genes).flatten()

    if inplace:
        high_var_x = x.T.iloc[topk_genes].T
        return high_var_x
    else:

        return topk_genes


def prepare_expr_data( df_list):
    '''
    If merge first is selected, dataframes are concatenated row-wise first, and the most variables genes are taken
    If not, most variables are selectes, and the intersection of those genes is then used to subset each df 
    Removing all-zero genes is 
    '''

    # First remove all zero genes
    print('Removing all zero genes')
    nonzero_df=[]
    for d in df_list:
        d = remove_allzero(d)
        nonzero_df+=[d]
    print('shape after...')
    for d in nonzero_df:
        print(d.shape)
    
    
    # First remove all zero genes
    print('Removing all zero genes')
    nonzero_df=[]
    for d in df_list:
        d = remove_allzero(d)
        nonzero_df+=[d]
    print('shape after...')
    for d in nonzero_df:
        print(d.shape)
    
    # Second select common genes between them

    # Second select 30k most variable genes
    print('Second select 30k most variable genes')

    df_list_30k = []
    for df in nonzero_df:
        df = high_variance(df,k=30000,inplace=True)
        df_list_30k+=[df]
    
    print('shape after...')
    for d in df_list_30k:
        print(d.shape)
    
    # Third select common genes between them
    print('Third Selecting common genes between them')
    gene_intersected_df_list = gene_intersection(dfs=df_list_30k)
    print('shape after...')
    
    for d in gene_intersected_df_list:
        print(d.shape)
    
    return gene_intersected_df_list


class preprocessing():

    def __init__(self):
        conversion_file='./data_oldtest/ensembl_hugo.tsv'

        self.gene_length=dict()
        self.ensemble_to_hugo_dct=dict()
        with open(conversion_file, 'r') as f:
            lines=f.readlines()
            for line in lines[1:]:
                line=line.split()
                length=float(line[2])/1000 # numbers in kilobases
                hugo=line[0]
                ensemble=line[1]
                self.gene_length[ensemble]=length
                self.ensemble_to_hugo_dct[ensemble]=hugo

    def RPKM(self, df):
        # for single end sequencing
        #should add RPKM as well
        # total number of reads for each sample
        # divide that total with 1000000 = scaling factor
        # divide each cell in the matrix by the scaling factor
        # divide each gene (column) by the genes length
        pass

    def FPKM(self, df):
        # for pair end sequencing
        # FPKM keeps track of the fragments that have two reads, and
        # does not double count
        # i think the rest of the process is the same as RPKM
        pass

    def TPM(self, df):
        import tqdm
        #df needs to be cells by genes
        #genes need to be in ensembl space

        #calculating reads per kilobase (RPK) for each gene
        for gene in tqdm.tqdm(df.columns):
            if gene not in self.gene_length.keys():
                df=df.drop(columns=[gene])
            else:
                length=self.gene_length[gene]
                df[gene]=df[gene]/float(length)

        scalling_factor=df.values.sum(axis=1)/1000000 #sums each row (samples) and dvides by 1 million

        assert len(scalling_factor)==df.shape[0]
        for i,sample in enumerate(df.index):
            df.iloc[i]=df.loc[sample]/scalling_factor[i]
        return df #cells by genes

    
    def ensembl_to_hugo(self, df):
        # df needs to be cells by genes
        # genes need to be in ensembl space

        print(df.shape)
        ensemble_genes=df.index #ensembl ids from df
        hugo_genes=[]
        nan_count=0
        for ensembl in ensemble_genes:
            try:
                hugo=self.ensemble_to_hugo_dct[ensembl]
                hugo_genes+=[hugo]
            except KeyError:
                nan_count+=1
                hugo_genes+=[np.nan]

        nan_bool=(np.array(hugo_genes)!='nan')
        print(nan_bool)
        gene_renaming_dict=dict(zip(ensemble_genes, hugo_genes))
        df=df.rename(index=gene_renaming_dict)#nans included
        df=df.loc[nan_bool] #nans excluded 
        print(df.shape)
        df=df.T #cells by genes
        return df
