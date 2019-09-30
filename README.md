# Ribo-deplete vs PolyA Library detection
    Simple classifier for detecting ribo-deplete libraries from polyA libraries
---

# Usage

1. Pull the image:
```
docker pull ioannisa92:ribo_vs_polya
```
2. Run the following command to mount your data files, and export the results:
```
docker run -it -v {your_local_outdir}:/app/out/ -v {your_local_datadir}:/app/data/ --rm ribo_test -i /app/data/{your_fn} -o ./out/{yout_ouput.tsv}
```
