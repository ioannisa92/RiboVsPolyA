#! /usr/bin/env python
from data_pp import *
import pandas as pd
import numpy as np

def select_mostvar(dfs, fns=None, save=True)
    '''
    scripts selects top 30k most var genes across all dfs
    dfs; list - list of dataframes
    fbs; list - list of filenames for saving
    
    Returns
    -------
    dfs; list - list of dataframes but subsetted for top 30k
    
    '''
    df_labels = np.arange(len(dfs))
    labels = []
    for i in df_labels:
        df_label = dfs[i].shape[0]*[i]
        labels += [labels]
    labels = np.array(labels)
    
    new_df = pd.concat[dfs, axis=0]
    new_df = all_data = remove_allzero(new_df)
    new_df = high_variance(new_df,k=30000,inplace=True)
    
    dfs = []
    for label in df_labels:
        df = new_df.iloc[labels==label]
        dfs +=[df]
    
    if save and fns:
        for i,df in enumerate(dfs):
            df.to_csv(fn[i]+".top30k", sep='\t')
    else:
        raise ValueError("No filename provided. Cannot save")
    
    return dfs
        
    

def select_random(dfs, fns=None, save=True):
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
    
    if save and fns:
        for i,df in enumerate(dfs):
            
            df.to_csv(fn[i]+".reduced", sep='\t')
    else:
        raise ValueError("No filename provided. Cannot save")        
    return new_dfs

def merge_data(dfs, fn=None, save=True):
    # Function takes in reduced polyA dataset and ribo dataset
    # Datasets are merged into one
    # Labels are created
    # Ribo = 1
    # Poly = 0
    
    df_labels = np.arange(len(dfs))
    all_labels = []
    for i in df_labels:
        df_label = dfs[i].shape[0]*[i]
        all_labels += [labels]
    all_labels = np.array(labels)

    all_data = pd.concat(dfs)
    all_labels = pd.DataFrame(all_labels, index=all_data.index, columns=['Ribo'])
    
    if save and fn:
            
        df.to_csv(fn, sep='\t')
        all_labels.to_csv(fn+"Labels.tsv", sep='\t')
    else:
        raise ValueError("No filename provided. Cannot save")
    
    
    return all_data, all_labels

def main():
    global DATADIR
    DATADIR = '../data_test/'
    ribo = DATADIR+"TreehousePEDv9_Ribodeplete_unique_hugo_log2_tpm_plus_1.2019-03-25.tsv" 
    poly = DATADIR+"TumorCompendium_v10_PolyA_hugo_log2tpm_58581genes_2019-07-25.tsv"
    
    dfs = []
    fns = [ribo, poly]
    
    for fn in fns:
        df = pd.read_csv(fn, index_col=0, sep='\t').T #(samples x genes)
        dfs +=[df]

    dfs = select_mostvar(dfs, fns=fns)
    dfs = select_random(dfs, fns=fns)
    all_data, all_labels = (dfs, fns="MergedData_Unbalanced.tsv")
    
    

if __name__ == "__main__":
    main()
