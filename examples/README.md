# RiboVsPolyA_analysis
Analysis notebooks for RiboVsPolyA [repo](https://github.com/ioannisa92/RiboVsPolyA)
---

# Classification Setup
Two classifiers were developed:
* A classifier that was trained on Ribo-deplete and PolyA libaries, without balancing for disease prevalence (**referred to as run1**)
* A classifier that was trained on the same data, however the PolyA compendium was split to reflect the disease prevalence in Ribo-deplete libraries (**referred to as run2**)

# Data pre-processing
[data_preprocessing](https://github.com/ioannisa92/RiboVsPolyA/tree/master/examples/data_processing) contains two notebooks showing:
  * BalanceDisease.ipynb: shows how diseases were balanced between PolyA and RiboD
  * UnbalancedDisease.ipynb: shows non-balanced diseases between the two datasets
    * Notebook contains Poly_reduced.csv which represents 361 randomly selected samples from the [Treehouse PolyA Compendium](https://treehousegenomics.soe.ucsc.edu/public-data/#tumor_v10_polyA)


# Balanced (Run1) Classification Analysis
[Balanced RF Analysis Notebook](https://github.com/ioannisa92/RiboVsPolyA/blob/master/examples/RF_train_Balanced.ipynb) shows optimization and performance of the disease *balanced* classifier

# Unbalanced (Run2) Classification Analysis
[Unalanced Analysis Notebook](https://github.com/ioannisa92/RiboVsPolyA/blob/master/examples/RF_train_Unbalanced.ipynb) shows optimization and performance of the disease *unbalanced* classifier

# Selecting the best model
[Cross Validation Analysis Notebook](https://github.com/ioannisa92/RiboVsPolyA/blob/master/examples/RF_train_Unbalanced.ipynb) shows cross validation analysis with the balanced RF classifier. Best model across folds is selected based on best performance.

# openPBTA PolyA - Applied Classifier
[openPBTA_polyA.ipynb](https://github.com/ioannisa92/RiboVsPolyA/blob/master/examples/openPBTA_polyA.ipynb) shows application  and performance of both blanced and unbalanced models on the openPBTA polyA cohort.

# openPBTA RiboD - Applied Classifier
[openPBTA_riboD.ipynb](https://github.com/ioannisa92/RiboVsPolyA/blob/master/examples/openPBTA_riboD.ipynb) shows application  and performance of both blanced and unbalanced models on the openPBTA riboD cohort.
