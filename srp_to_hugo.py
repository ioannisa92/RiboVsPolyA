import data_pp
import os
import pandas as pd
import numpy as np
data = './SRP_data/refine_bio_SRP_data/'

for f in os.listdir(data):
    if f.startswith("SRP"):
        print('running', f)
        path = os.path.join(data, f+'/'+f+'.abundance.HUGO.tsv')
        #pp = data_pp.preprocessing()
        df = pd.read_csv(path, index_col=0)
        #df = pp.ensembl_to_hugo(df)
        print(df.head())
        print('applying and writing HUGO file')
        df = df.apply(lambda x:np.log2(x+1))
        df.to_csv(os.path.join(data,f+'/'+f+'.log2TPM_plus1.HUGO.tsv'), sep='\t')
