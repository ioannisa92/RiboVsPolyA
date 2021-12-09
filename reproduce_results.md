# Steps to Reproduce Results

## Installation
This project makes use of python3 and conda. Make sure you have conda installed, and use the following commands to create the conda environment and clone the repo.

```
conda create -n ribopolya python=3.6
conda activate ribopolya
git clone https://github.com/ioannisa92/RiboVsPolyA.git
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
