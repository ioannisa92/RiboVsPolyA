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
docker run -it -v {your_local_outdir}:/app/out/ -v {your_local_datadir}:/app/data/ --rm ribo_vs_polya -i /app/data/{your_input_fn} -o /app/out/{your_ouput_fn}
```
The output from the classifier will look something like the following:
```
SampleID        Ribo(1) Proba_0                 Proba_1
Sample1         0.0     0.7542999600155401      0.24570003998445986
Sample2         1.0     0.345707572599551       0.654292427400449
Sample3         1.0     0.46276063859515026     0.5372393614048496
Sample4         1.0     0.31682082492996877     0.6831791750700313
Sample5         1.0     0.35819045535178123     0.641809544648219
Sample6         1.0     0.20026228215007455     0.7997377178499254
Sample7         0.0     0.566463652051628       0.43353634794837204
Sample8         0.0     0.8166816735225906      0.18331832647740934
Sample9         0.0     0.8102647319103403      0.18973526808965965
Sample10        0.0     0.8132647319103403      0.18673526808965965
Sample11        1.0     0.3009267488489455      0.6990732511510545
Sample12        0.0     0.5874583872497835      0.4125416127502163
```
