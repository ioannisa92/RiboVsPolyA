#!/usr/bin/env python
# coding: utf-8

# # The following notebook merges PolyA and RiboD datasets
# * Datasets are unbalanced in terms of disease
# * PolyA datasets has many more samples compared to RiboD
# * Balacing of diseases is done based on the disease prevalence of RiboD
# 


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
global DATADIR
DATADIR = './data_test/'

# ## Loading PolyA and RiboD gene expression data


# the following files were prepared during setup.py
# both Poly.tsv and Ribo.tsv are described by the same genes
poly = pd.read_csv(DATADIR+'TumorCompendium_v10_PolyA_hugo_log2tpm_58581genes_2019-07-25.tsv', sep='\t', index_col=0).T # (samples,genes)
ribo = pd.read_csv(DATADIR+'TreehousePEDv9_Ribodeplete_unique_hugo_log2_tpm_plus_1.2019-03-25.tsv', sep='\t', index_col=0).T # (sampls,genes)


poly.shape
ribo.shape



poly_clinical = pd.read_csv('./data_test/clinical_TumorCompendium_v10_PolyA_2019-07-25.tsv', sep='\t', index_col=0)
ribo_clinical = pd.read_csv('./data_test/TreehousePEDv9_Ribodeplete_clinical_metadata.2019-03-25.tsv', sep='\t', index_col=0)

poly_single_disease = poly_clinical.disease.value_counts().index.values[(poly_clinical.disease.value_counts()==1)]
ribo_single_disease = ribo_clinical.disease.value_counts().index.values[(ribo_clinical.disease.value_counts()==1)]


# ## Filling any NA values in the clinical files
# * one sample with NA values


poly_clinical_dropped = poly_clinical.loc[~poly_clinical.disease.str.contains('|'.join(poly_single_disease)).fillna(True)] #one na sample
ribo_clinical_dropped = ribo_clinical.loc[~ribo_clinical.disease.str.contains('|'.join(ribo_single_disease)).fillna(True)] #one na sample


# ## Collecting common diseases from PolyA and RiboD

common_diseases = set(ribo_clinical_dropped.disease.value_counts().index).intersection(poly_clinical_dropped.disease.value_counts().index)



# Displaying common diseases
(common_diseases)


# ## Selecting samples from PolyA and RiboD that match common_diseases


poly_masked = np.arange(poly_clinical_dropped.shape[0])
ribo_masked = np.arange(ribo_clinical_dropped.shape[0])
poly_clinical_disease_common_idx = []
ribo_clinical_disease_common_idx = []

for disease in common_diseases:
    poly_disease_booleans = (poly_clinical_dropped.disease==disease).values
    ribo_disease_booleans = (ribo_clinical_dropped.disease==disease).values
    poly_disease_idx = poly_masked[poly_disease_booleans]
    ribo_disease_idx = ribo_masked[ribo_disease_booleans]

    poly_clinical_disease_common_idx += list(poly_disease_idx)
    ribo_clinical_disease_common_idx += list(ribo_disease_idx)
    
poly_clinical_disease_common = poly_clinical_dropped.iloc[poly_clinical_disease_common_idx]
ribo_clinical_disease_common = ribo_clinical_dropped.iloc[ribo_clinical_disease_common_idx]


# # Checking prevalence of diseases in both datasets...

poly_clinical_disease_common.disease.value_counts()/poly_clinical_disease_common.disease.value_counts().sum()

ribo_clinical_disease_common.disease.value_counts()/ribo_clinical_disease_common.disease.value_counts().sum()

# ## Diseases are still not balanced


desired_prevalence = ribo_clinical_disease_common.disease.value_counts()


# ## Picking samples in expression files that are match common diseases

# picking polyA samples belonging in common_diseases
poly_disease_common = poly.loc[poly_clinical_disease_common.index]

# picking riboD samples belonging in common_diseases
ribo_disease_common = ribo.loc[ribo_clinical_disease_common.index]


# ## Subsampling from PolyA based on RiboD prevalence

poly_subsampled = []
for disease in desired_prevalence.index:
    sample = desired_prevalence.loc[disease] # disease prevalence in RiboD
    n = poly_disease_common.loc[poly_clinical_disease_common.disease==disease].shape[0] # number of polyA samples beloging in common disease
    
    if sample <=n:
        # if number of riboD samples belogning to disease is less than polyA samples belong to disease
        # then sample from polyA samples as big as the number of samples in riboD 
        disease_subsample = poly_disease_common.loc[poly_clinical_disease_common.disease==disease].sample(n=sample)
        
    else:
        disease_subsample = poly_disease_common.loc[poly_clinical_disease_common.disease==disease]
    
    poly_subsampled +=[disease_subsample]

poly_subsampled_final = pd.concat(poly_subsampled, axis=0) # subsampled polyA dataframe based on riboD disease prevalence
poly_clinical_disease_common_sumbsampled_final = poly_clinical_disease_common.loc[poly_subsampled_final.index] # modifying polyA clinical file to match the subsampled samples


assert poly_subsampled_final.columns.values.tolist() == ribo_disease_common.columns.values.tolist()


# ## Merging processed PolyA and RiboD samples into one file for downstream analysis
# #### Labelling:
# * Ribo samples = 1
# * Poly samples = 0


ribo_labels = ribo_disease_common.shape[0]*[1]
poly_labels = poly_subsampled_final.shape[0]*[0]
all_labels = ribo_labels+poly_labels

merged_disease_common = pd.concat([ribo_disease_common, poly_subsampled_final], axis=0)
merged_labels = pd.DataFrame(all_labels, index = merged_disease_common.index, columns = ['Ribo'])

# saving file to disk
merged_disease_common.to_csv('./data_test/MergedData_Balanced.tsv', sep='\t')
merged_labels.to_csv('./data_test/MergedLabels_Balanced.tsv', sep='\t')

merged_disease_common.shape

# ## Now diseases are balanced in both datasets

(poly_clinical_disease_common_sumbsampled_final.disease.value_counts()/poly_clinical_disease_common_sumbsampled_final.disease.value_counts().sum()).plot(kind='bar')
plt.title('Final Poly Disease Prevalence', fontsize=15)
plt.xticks(rotation=45)
plt.show()
plt.close()

(ribo_clinical_disease_common.disease.value_counts()/ribo_clinical_disease_common.disease.value_counts().sum()).plot(kind='bar')
plt.title('Final Ribo Disease Prevalence', fontsize=15)
plt.xtcks(rotation=45)
plt.show()
plt.close()

