REFINEBIODATA="./data/refine_bio_SRP_data/"
TREEHOUSEDATA="./data/treehouse_SRP_data/"

if [ -d "$REFINEBIODATA" ]; then
  # Take action if $DIR exists. #
  echo "${REFINEBIODATA} already exists"
else
    mkdir -p $REFINEBIODATA
fi

if [ -d "$TREEHOUSEDATA" ]; then
  # Take action if $DIR exists. #
  echo "${TREEHOUSEDATA} already exists"
else
    mkdir -p $TREEHOUSEDATA
fi

# Download SRP data from figshare
echo Downloading SRP data processed via Treehouse pipeline

wget -O ${TREEHOUSEDATA}SRP026013_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193727

wget -O ${TREEHOUSEDATA}SRP055411_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193730

wget -O ${TREEHOUSEDATA}SRP058841_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193733

wget -O ${TREEHOUSEDATA}SRP064410_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193736

wget -O ${TREEHOUSEDATA}SRP109549_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193739

wget -O ${TREEHOUSEDATA}SRP127360_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193742

wget -O ${TREEHOUSEDATA}SRP130971_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193745

wget -O ${TREEHOUSEDATA}SRP132968_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193748

wget -O ${TREEHOUSEDATA}SRP183700_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193751

echo Downloading SRP data processed via refine.bio pipeline

wget -O ${REFINEBIODATA}SRP026013_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193775

wget -O ${REFINEBIODATA}SRP055411_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193781

wget -O ${REFINEBIODATA}SRP058841_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193784

wget -O ${REFINEBIODATA}SRP064410_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193790

wget -O ${REFINEBIODATA}SRP109549_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193799

wget -O ${REFINEBIODATA}SRP130971_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193802

wget -O ${REFINEBIODATA}SRP132968_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193805

wget -O ${REFINEBIODATA}SRP183700_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193808
