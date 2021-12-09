# Ribo-deplete vs PolyA Library detection

Simple classifier for distinguishing ribo-deplete libraries from polyA libraries

In the [examples folder](https://github.com/ioannisa92/RiboVsPolyA/tree/master/examples), jupyter notebooks are provided for:
  * Data pre-processing (balancing disease prevalanecne)
  * Training Random Forest (RF) model on unbalanced and balanced data. Optimisation procedure also shown
  * The notebooks also have the corresponding script version under [scripts](https://github.com/ioannisa92/RiboVsPolyA/tree/master/scripts)

# Installation
Our model runs with python3. We recommend to use a recent version of python3 (eg. python>=3.6). \
We recommend using conda to create a virtual environment. \
Follow the steps bellow to install this repo:

```
conda create -n ribopolya python=3.6
conda activate ribopolya
git clone https://github.com/ioannisa92/RiboVsPolyA.git
```

Running the following to install and download the necessary data:
```
bash setup.sh
```
Then run `setup.sh` to download all the necessary data, convert the data to usable format, and create a balanced dataset.

## Usage
1. Run `logistic_classifier.py` to generate logistic classifier based on riboD and polyA dataset and save .sav file to be used later.
2. Run `gscv.sh` to obtain a grid search to find the optimal hypterparamters to train the model.
    * Note: This process is very memory intensive, ensure that your computer has more than 14gb of memory to guarantee sucess of the script.
    * This will generate a file named `rf_cv_best_params.npy` which is binary file holding the best hyperparamter data.
3. Run `logistic_deploy.sh` to generate logistic classifier results on SRP data to compare random forest results to.
   * This will generate outputs for each of the SRP sample files for both treehouse, non treehouse data, and store them accordingly under `results/`
4. Run `RF_CV.ipynb` under `examples/` to generate various random forest models of various depths to be used later for comparision.
5. Run `openPBTA_classifier_results.ipynb` and `openPBTA_polyA_riboD.ipynb`  to test generated model performance on openPBTA data
    * This tumor data for which the random forest model is trained better for, so the results will be more accurate.
6. Run `run_SRP.sh` to generate random forest results on SRP data
   * This will generate outputs for each of the SRP sample files for both treehouse, non treehouse data, and store them accordingly under `results/`
7. Test accuracy of random forest model on non-tumor data by running `SRP#` notebooks under `examples/`.
    * Each notebook will generate predicted labels for each sample and generate an accuracy score for both the random forest and logistic classifier for comparision
8. To compare accuracy for tumor data the openPBTA notebooks can be consulted, while the accuracy for non-tumor specific tumor data can be found in the SRP notebooks
---

# Docker Usage

## Pull the image:

```
docker pull ioannisa92/ribo_vs_polya
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
