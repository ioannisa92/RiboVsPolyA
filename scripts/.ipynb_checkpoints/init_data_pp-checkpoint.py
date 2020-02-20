#! /usr/bin/env python
from data_pp import *
import pandas as pd
import numpy as np

def subset_genes():
    # Function reads in RiboD and PolyA expression file
    # Genes are intersected to find common genes
    # Genes are subsetted in both files
    print("reading riboD expression file...")
    ribo = "./data_test/TreehousePEDv9_Ribodeplete_unique_hugo_log2_tpm_plus_1.2019-03-25.tsv" 
    ribo_df = pd.read_csv(ribo, index_col=0, sep='\t').T #(samples x genes)

    #reading in PolyA file
    print("reading polyA expression file...")
    poly = "./data_test/TumorCompendium_v10_PolyA_hugo_log2tpm_58581genes_2019-07-25.tsv"
    poly_df = pd.read_csv(poly, index_col=0, sep='\t').T #(samples x genes)

    # getting genes shared in both datsets
    # subsetting original files
    poly_df, ribo_df = prepare_expr_data([poly_df, ribo_df])
    
    #assert len(poly_df.columns.values) == 25924 # number is known prior to running the script
    #assert len(ribo_df.columns.values) == 25924
    
    with open('./data_test/ClassifierGenes', 'w') as f:
        for gene in poly_df.columns.values:
            f.write(gene+'\n')

    return poly_df, ribo_df

def reduce_poly(poly_df, ribo_df):
    # Function takes in the polyA and riboD dataset
    # Loads the polyA clinical file
    # Subsets randomly both expression and clinical PolyA based on RiboD sample population
    
    poly_clinical = "./data_test/clinical_TumorCompendium_v10_PolyA_2019-07-25.tsv"
    poly_clinical_df = pd.read_csv(poly_clinical, sep='\t', index_col=0)[['disease']]

    ribo_n = ribo_df.shape[0] #number of riboD samples
    # randomly choosing samples from poly_A dataset 
    # based on the number of samples 
    reduced_poly_samples = np.random.choice(poly_df.index, ribo_n)
    
    #subsetting original file
    reduced_poly_df = poly_df.loc[reduced_poly_samples]

    #subsetting clinical file with same samples
    reduced_poly_clinical_df = poly_clinical_df.loc[reduced_poly_samples]
    return reduced_poly_df, reduced_poly_clinical_df

def merge_data(reduced_poly_df, ribo_df):
    # Function takes in reduced polyA dataset and ribo dataset
    # Datasets are merged into one
    # Labels are created
    # Ribo = 1
    # Poly = 0
    
    ribo_labels = ribo_df.shape[0]*[1]
    poly_labels = reduced_poly_df.shape[0]*[0]
    all_labels = ribo_labels+poly_labels

    all_data = pd.concat([ribo_df, reduced_poly_df])
    all_labels = pd.DataFrame(all_labels, index=all_data.index, columns=['Ribo'])
    
    return all_data, all_labels

def main():
    DATADIR = './data_test/'
    poly_df, ribo_df = subset_genes()
    
    print('saving gene-subsetted dataframes with same genes to disk...')
    poly_df.to_csv(DATADIR+"Poly.tsv", sep='\t')
    ribo_df.to_csv(DATADIR+"Ribo.tsv", sep='\t')

    reduced_poly_df, reduced_poly_clinical_df = reduce_poly(poly_df, ribo_df) 
    print('saving reduced poly datasets to disk...')
    reduced_poly_df.to_csv(DATADIR+"Poly_reduced.tsv", sep='\t')
    reduced_poly_clinical_df.to_csv(DATADIR+"Poly_clinical_reduced.tsv", sep='\t')
    
    all_data, all_labels = merge_data(reduced_poly_df, ribo_df)
    print("saving merged data and labels to disk...")
    all_data.to_csv(DATADIR+"MergedData_Unabalanced.tsv", sep='\t')
    all_labels.to_csv(DATADIR+"MergedLabels_Unabalanced.tsv", sep='\t')

if __name__ == "__main__":
    main()
