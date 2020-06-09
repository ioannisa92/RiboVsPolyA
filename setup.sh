# create data dolder
mkdir data_test
mkdir results

echo Downloading Expression and Cilinical PolyA and RiboD files...
# Download Treehouse PolyA, RiboD expression files
wget --quiet -O ./data_test/TumorCompendium_v10_PolyA_hugo_log2tpm_58581genes_2019-07-25.tsv https://xena.treehouse.gi.ucsc.edu/download/TumorCompendium_v10_PolyA_hugo_log2tpm_58581genes_2019-07-25.tsv

wget --quiet -O ./data_test/TreehousePEDv9_Ribodeplete_unique_hugo_log2_tpm_plus_1.2019-03-25.tsv https://xena.treehouse.gi.ucsc.edu/download/TreehousePEDv9_Ribodeplete_unique_hugo_log2_tpm_plus_1.2019-03-25.tsv

# Download PolyA, RiboD clinical files
wget --quiet -O ./data_test/clinical_TumorCompendium_v10_PolyA_2019-07-25.tsv https://xena.treehouse.gi.ucsc.edu/download/clinical_TumorCompendium_v10_PolyA_2019-07-25.tsv
wget --quiet -O ./data_test/TreehousePEDv9_Ribodeplete_clinical_metadata.2019-03-25.tsv https://xena.treehouse.gi.ucsc.edu/download/TreehousePEDv9_Ribodeplete_clinical_metadata.2019-03-25.tsv

# echo Creating Unbalanced dataset...
# run script that selects random samples from PolyA to create MergedData_reduced.tsv, and MergedLabels_reduced.tsv
# python ./scripts/merge_unbalanced.py

echo Creating Balanced dataset...
#run script that selects random samples from PolyA to create MergedData_reduced.tsv, and MergedLabels_reduced.tsv
python ./scripts/merge_balanced.py



echo DONE
# make notebooks under examples to take these files as input

