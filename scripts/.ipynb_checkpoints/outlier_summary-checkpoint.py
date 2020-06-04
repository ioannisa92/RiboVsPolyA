#! /usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

class Summary:
        
    def __init__(self, outlier_fn=None, sep='\t'):
        
        
        self.genes = []
        self.transcripts = []
        
        self.all_info = {} 
        with open(outlier_fn, 'r') as f:
            lines = f.readlines()
            

            for i,line in enumerate(lines):
                if i==0:
                    self.samples=line.split('\t')[1:]
                else:
                    line = line.split(sep)
                    transcript_id = line[0].split('_')[0].strip()
                    self.transcripts +=[transcript_id]
                    gene = line[0].split('_')[1].strip()
                    self.genes += [gene]
                    self.all_info[gene] = line[1:]

        df = pd.read_csv(outlier_fn, sep='\t')
        df['gene_id'] = self.genes
        self.df = df.set_index('gene_id')
        
    def load_meta(self, path, sep='\t'):
        '''
        Assumes file is tab delimited
        '''
        
        if isinstance(path, pd.DataFrame):
            df = path
        elif 'tsv'==path[-3:]:
            df = pd.read_csv(path, sep='\t', index_col=0)
    
        common_samples = set(self.df.columns).intersection(df.index)
        
        self.meta = df.loc[common_samples]
        print(self.df.shape)

        self.df = self.df.T.loc[common_samples].T
        print(self.df.shape)

    def count_id(self,symbols=list()):
        if not  isinstance(symbols, list):
            raise ValueError("Variable symbols needs to be a list")
        new_all_info = {} 
        
        for gene, categories in self.all_info.items():
            
            new_all_info[gene] = [x for x in categories if x in symbols]
            
        self.all_info = new_all_info 
                    
    
    def filter_outliers(self,desired_genes):
        '''
        Method takes in a txt file with genes that need to be retained from 
        the original file
        ''' 
        filtered_outliergene_samples = {}
        for gene, samples in self.all_info.items():
            if gene in desired_genes:
                filtered_outliergene_samples[gene] = samples

        self.all_info = filtered_outliergene_samples

    def plot_outliers(self, figsize = (10,5), title=None, n=None, normalize=False, meta_column=None):
        groups = self.meta.groupby(meta_column).groups
        
        count_dict_list = {}  #in case more than one id is passed to count_id AND meta_column is passed, a bar plot for each group in meta_column will be made
        count_dict = {}
        if meta_column is not None:
            for gene, ids in self.all_info.items():
                count_dict[gene] = {} 
                if len(set(ids)) ==1:
                    outlier_id = ids[0]
                    for group,samples in groups.items():
                        for sample in samples:
                            if self.df.loc[gene,sample]==outlier_id:
                                count_dict[gene][group] = count_dict[gene].get(group,0)+1
                elif len(set(ids)) !=1:
                    outlier_ids = set(ids)
                    for outlier_id in outlier_ids:
                        count_dict = {}
                        for group,samples in groups.items():
                            for sample in samples:
                                if self.df.loc[gene,sample]==outlier_id:
                                    count_dict[gene][group] = count_dict[gene].get(group,0)+1
                        count_dict_list[outlier_id]= count_dict
                
        else:
            for gene, ids in self.all_info.items():
                count_dict[gene] = {}
                for outlier_id in ids:
                    count_dict[gene][outlier_id] = count_dict[gene].get(outlier_id,0) +1
                
        count_mat = pd.DataFrame.from_dict(count_dict).fillna(0).T
        
        count_mat = count_mat.iloc[count_mat.sum(axis=1).argsort()[::-1]]
        
        if normalize:
            total = count_mat.values.sum()
            count_mat /=total
        if n is not None:
            count_mat = count_mat.head(n)
        
        fig, axes = plt.subplots(figsize=figsize)
        cmap = cm.get_cmap('tab20') # Colour map (there are many others)
        count_mat.plot(kind='bar', stacked=True, ax=axes,cmap=cmap)
        plt.ylabel('Samples', fontsize=15)
        plt.legend(bbox_to_anchor=(1.3, 1.05))
        plt.show()
        plt.close()
             


if __name__ == '__main__':
    c = Summary(outlier_fn='../data_test/rsem-tpm-stranded-gene_expression_outliers.tsv')
    print(len(c.failed_samples))
    #for k,v in c.outliergene_samples.items():
    #    print(k, len(v))
