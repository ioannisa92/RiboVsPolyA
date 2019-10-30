# Ribo-deplete vs PolyA Library detection

Simple classifier for distinguishing ribo-deplete libraries from polyA libraries

---
# Usage

## Pull the image:

```
docker pull ioannisa92:ribo_vs_polya
```

## Run the following command to mount your data files, and export the results:

```
docker run -it -v {your_local_outdir}:/app/out/ -v {your_local_datadir}:/app/data/ --rm ribo_vs_polya -i /app/data/{your_fn} -o /app/out/{your_ouput.tsv}
```
