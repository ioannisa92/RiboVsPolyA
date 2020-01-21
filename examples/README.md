# RiboVsPolyA_analysis
Analysis notebooks for RiboVsPolyA [repo](https://github.com/ioannisa92/RiboVsPolyA)
---

# Classification Setup
Two classifiers were developed:
* A classifier that was trained on Ribo-deplete and PolyA libaries, without balancing for disease prevalence (**referred to as run1**)
* A classifier that was trained on the same data, however the PolyA compendium was split to reflect the disease prevalence in Ribo-deplete libraries (**referred to as run2**)

[Random Forest Script](https://github.com/ioannisa92/RiboVsPolyA_analysis/blob/master/RF.py) shows how the classifier was setup, and the save file (.npy) of how the results are saved

# Rank Correlation Analysis
[Corellation Notebook](https://github.com/ioannisa92/RiboVsPolyA_analysis/blob/master/RankCorrelation.ipynb) shows the correlation of the rank of genes as determined by importance scoring from run1 and run2 classifiers

# Run1 Classification Analysis
[Run1 Analysis Notebook](https://github.com/ioannisa92/RiboVsPolyA_analysis/blob/master/ResultsAnalysis_run1.ipynb) shows the performance of the disease *unbalanced* classifier

# Run2 Classification Analysis
[Run2 Analysis Notebook](https://github.com/ioannisa92/RiboVsPolyA_analysis/blob/master/ResultsAnalysis_run2.ipynb) shows teh performance of the disease *balanced* classifier
