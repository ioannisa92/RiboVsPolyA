# Create data folders
DATADIR="./data/"
RESDIR="./results/"
PLOTDIR="./plots/"
MODELDIR="./models/"

if [ -d "$DATADIR" ]; then
  # Take action if $DIR exists. #
  echo "${DATADIR} already exists"
else
    mkdir $DATADIR
fi

if [ -d "$RESDIR" ]; then
  # Take action if $DIR exists. #
  echo "${RESDIR} already exists"
else
    mkdir $RESDIR
fi

if [ -d "$PLOTDIR" ]; then
  # Take action if $DIR exists. #
  echo "${PLOTDIR} already exists"
else
    mkdir $PLOTDIR
fi

if [ -d "$MODELDIR" ]; then
  # Take action if $DIR exists. #
  echo "${MODELDIR} already exists"
else
    mkdir $MODELDIR
fi

echo Installing requirements...
python -m pip install --no-cache-dir -r requirements.txt

echo Downloading Expression and Clinical PolyA and RiboD files...
# Download Treehouse compendium PolyA, RiboD expression files
wget --quiet --show-progress -O ${DATADIR}TumorCompendium_v10_PolyA_hugo_log2tpm_58581genes_2019-07-25.tsv https://xena.treehouse.gi.ucsc.edu/download/TumorCompendium_v10_PolyA_hugo_log2tpm_58581genes_2019-07-25.tsv

wget --quiet --show-progress -O ${DATADIR}TreehousePEDv9_Ribodeplete_unique_hugo_log2_tpm_plus_1.2019-03-25.tsv https://xena.treehouse.gi.ucsc.edu/download/TreehousePEDv9_Ribodeplete_unique_hugo_log2_tpm_plus_1.2019-03-25.tsv

# Download PolyA, RiboD clinical files
wget --quiet --show-progress -O ${DATADIR}clinical_TumorCompendium_v10_PolyA_2019-07-25.tsv https://xena.treehouse.gi.ucsc.edu/download/clinical_TumorCompendium_v10_PolyA_2019-07-25.tsv
wget --quiet --show-progress -O ${DATADIR}TreehousePEDv9_Ribodeplete_clinical_metadata.2019-03-25.tsv https://xena.treehouse.gi.ucsc.edu/download/TreehousePEDv9_Ribodeplete_clinical_metadata.2019-03-25.tsv

echo Downloading openPBTA files...
wget --quiet --show-progress -O ${DATADIR}pbta-gene-expression-rsem-tpm.stranded.rds  https://s3.amazonaws.com/kf-openaccess-us-east-1-prd-pbta/data/release-v16-20200320/pbta-gene-expression-rsem-tpm.stranded.rds

wget --quiet --show-progress -O ${DATADIR}pbta-gene-expression-rsem-tpm.polya.rds  https://s3.amazonaws.com/kf-openaccess-us-east-1-prd-pbta/data/release-v16-20200320/pbta-gene-expression-rsem-tpm.polya.rds

echo Converting openPBTA files to tsv...
python ./scripts/rds_to_pandas.py -i ${DATADIR}pbta-gene-expression-rsem-tpm.stranded.rds -o ${DATADIR}pbta-gene-expression-rsem-log2tpm_plus_1.stranded.tsv

python ./scripts/rds_to_pandas.py -i ${DATADIR}pbta-gene-expression-rsem-tpm.polya.rds -o ${DATADIR}pbta-gene-expression-rsem-log2tpm_plus_1.polya.tsv

echo downloading SRP data
bash ./scripts/setup_SRP.sh

echo Creating Balanced dataset...
#run script that selects random samples from PolyA to create MergedData_reduced.tsv, and MergedLabels_reduced.tsv
python ./scripts/merge_balanced.py

echo Creating logistic classifier...
#run script that creates logistic classifier
python ./scripts/logistic_classifier.py

echo DONE
