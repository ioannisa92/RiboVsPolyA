# Scripts
* `rds_to_pandas.py`: converts R datastrutures into .tsv files
* `merge_balanced.py`:
    * file goes through clinical polyA and riboD data to find what diseases are given in that data
    * finds what diseases are common between both data sets
    * samples any samples that come from those disease from the polyA and riboD data from treehouse
    * subsamples from all data of same diseases to build new merged + balanced dataset
    * outputs 2 files to disk:
        1. merged_balanced_data: the actual data for each of the samples (gene expression)
        2. merged_balanced_labels: labels for the data if its riboD (1) or not (0)
    * creates plots of prevalence of each disesase in the merged + balanced datasets for polA and riboD
* `logistic_classifier.py`: generates a logistic classifier based on riboD and polyA datasets
* `data_pp.py`: converts ensembl gene ids to HGNC (Hugo gene ids)
* `RV_cv.py`: create and train the random forest classifier
    * TEST CODE TO THEN PORT OVER TO `RV_CF.ipynb`
    * metrics that model gets every time in cross-validation:
        * stratifiedKfold splits data by some criteria (ex. each fold has same num of disease)
        * accuracy: percentage of instances model got correct value
        * precision: fraction of true positives over total positives (true positives + false positives)
            * positive predictive accuracy for label
        * recall: fraction of true positives over useful outcomes of model (true positves + false negatives)
            * true positive rate for label
    * gridsearchcv parameters:
        * n_estimators: number of trees in forest
        * max_depth: max depth of each trees
        * min_samples_leaf: number of samples required to be a leaf node
        * min_samples_split: number of samples required to split internal node
    * parse through command line args and perform tasks based on them
* `RF_deploy.py`:
    * gene_checker: fills in 0s for gene entries in input file that exist in predetermined classifier genes
    * read in input file, format input file, apply model, save results
    * predict_proba: function that gives probability of each outcome in rows
