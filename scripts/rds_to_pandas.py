
import pyreadr
import argparse

def to_pandas(filename):
    df = pyreadr.read_r(filename)[None]
    df = df.set_index(df.columns[0])
    old_index = df.index.tolist()
    new_index = list(map(lambda x:x.split('_')[-1], old_index))
    rename_dict = dict(zip(old_index, new_index))
    df = df.rename(index=rename_dict)
    del df.index.name 
    return df.T # (samples, genes)


    
if __name__ == '__main__':
    
    ########----------------------Command line arguments--------------------##########
    parser = argparse.ArgumentParser(description="Arguments for converting rds to tsv")

    parser.add_argument('-i', '--input', default=None, type=str, required=True, help='Input expression file (samples x genes')
    parser.add_argument('-o', '--output', default='out.tsv', type=str, required=False, help='TSV Output prediction file')
    args=parser.parse_args()

    ########----------------------Command line arguments--------------------##########

    rds_fn = args.input
    rds_out = args.output

    df = to_pandas(rds_fn)
    df.to_csv(rds_out, sep='\t')
