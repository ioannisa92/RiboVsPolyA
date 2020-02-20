#! /usr/bin/env python
from data_pp import *
import pandas as pd
import numpy as np

def select_mostvar(dfs, fns=None):
    '''
    scripts selects top k most var genes across all dfs
    dfs; list - list of dataframes
    fbs; list - list of filenames for saving
    
    Returns
    -------
    dfs; list - list of dataframes but subsetted for top 30k
    
    '''
    original_shapes = []
    for df in dfs:
        original_shapes += [df.shape[0]]
    
    new_df = pd.concat(dfs, axis=0)
    new_df = all_data = remove_allzero(new_df)
    new_df = high_variance(new_df,k=5000,inplace=True)
    
    new_dfs = []
    for i,df in enumerate(dfs):
        if i==0:
            df = new_df.iloc[:original_shapes[i]]
        elif i==len(new_dfs)-1:
            df = new_df.iloc[original_shapes[i-1]:]
        else:
            df = new_df.iloc[original_shapes[i-1]:original_shapes[i-1]+original_shapes[i]]

        new_dfs +=[df]
    
    return new_dfs
        
    

def select_random(dfs, fns=None):
    # Function takes in a list of dfs and finds the one with the least samples
    # all other dfs are randomly sampled based on the least samples

    smallest_shape = None
    for df in dfs:
        samples = df.shape[0]
        if smallest_shape is None or samples < smallest_shape:
            smallest_shape = samples
    new_dfs =[]
    for i,df in enumerate(dfs):
        if smallest_shape != df.shape[0]:
            if fns:
                print("Reducing "+fn[i])
            random_samples = np.random.choice(df.index, smallest_shape)
            df = df.loc[random_samples]
            new_dfs += [df]
        else:
            new_dfs +=[df]
    
    return new_dfs

def merge_data(dfs, fn=None):
    # Function takes in reduced polyA dataset and ribo dataset
    # Datasets are merged into one
    # Labels are created
    # Ribo = 1
    # Poly = 0
    
    df_labels = np.arange(len(dfs))
    all_labels = []
    for i in df_labels:
        df_label = dfs[i].shape[0]*[i]
        all_labels += [df_label]
    all_labels = np.array(all_labels).reshape(-1,1)

    all_data = pd.concat(dfs)
    all_labels = pd.DataFrame(all_labels, index=all_data.index, columns=['Ribo'])
    
    return all_data, all_labels

def main():
    global DATADIR
    DATADIR = '../data_test/'
    ribo = DATADIR+"TreehousePEDv9_Ribodeplete_unique_hugo_log2_tpm_plus_1.2019-03-25.tsv" 
    poly = DATADIR+"TumorCompendium_v10_PolyA_hugo_log2tpm_58581genes_2019-07-25.tsv"
    
    dfs = []
    fns = [poly, ribo]
    print("reading files") 
    for fn in fns:
        df = pd.read_csv(fn, index_col=0, sep='\t').T #(samples x genes)
        dfs +=[df]
    print("selecting most var")
    dfs = select_mostvar(dfs)
    for df in dfs:
        print(df.shape)
    dfs[0].to_csv(DATADIR+"Poly.tsv", sep="\t")
    dfs[1].to_csv(DATADIR+"Ribo.tsv", sep="\t")
    
    print("reducing datasets")
    dfs = select_random(dfs)
    for df in dfs:
        print(df.shape)

    dfs[0].to_csv(DATADIR+"Poly_reduced.tsv", sep="\t")

    all_data, all_labels = merge_data(dfs)
    all_data.to_csv(DATADIR+"MergedData_Unbalanced.tsv", sep="\t")
    all_labels.to_csv(DATADIR+"MergedLabels_Unbalanced.tsv", sep="\t")
    
    with open(DATADIR+"ClassifierGenes_unbalanced.txt", 'w') as f:
        for gene in all_data.columns:
            f.write(gene+'\n')    
if __name__ == "__main__":
    main()
