# create data dolder
mkdir data

# Download Treehouse PolyA, RiboD compendia
wget https://treehousegenomics.soe.ucsc.edu/public-data/#tumor_v10_polyA ./data/
wget https://treehousegenomics.soe.ucsc.edu/public-data/#v9publicribo ./data/

#run script that selects random samples from PolyA to create MergedData_reduced.tsv, and MergedLabels_reduced.tsv

