REFINEBIODATA="./SRP_data/refine_bio_SRP_data/"
TREEHOUSEDATA="./SRP_data/treehouse_SRP_data/"

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

mkdir ./${TREEHOUSEDATA}/SRP026013 && wget -O ${TREEHOUSEDATA}/SRP026013/SRP026013_log2TPM_plus4_HUGO.tsv https://ndownloader.figshare.com/files/27193727

mkdir ./${TREEHOUSEDATA}/SRP055411 && wget -O ${TREEHOUSEDATA}/SRP055411/SRP055411_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193730

mkdir ./${TREEHOUSEDATA}/SRP058841 && wget -O ${TREEHOUSEDATA}/SRP058841/SRP058841_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193733

mkdir ./${TREEHOUSEDATA}/SRP064410 && wget -O ${TREEHOUSEDATA}/SRP064410/SRP064410_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193736

mkdir ./${TREEHOUSEDATA}/SRP109549 && wget -O ${TREEHOUSEDATA}/SRP109549/SRP109549_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193739

mkdir ./${TREEHOUSEDATA}/SRP127360 && wget -O ${TREEHOUSEDATA}/SRP127360/SRP127360_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193742

mkdir ./${TREEHOUSEDATA}/SRP130971 && wget -O ${TREEHOUSEDATA}/SRP130971/SRP130971_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193745

mkdir ./${TREEHOUSEDATA}/SRP132968 && wget -O ${TREEHOUSEDATA}/SRP132968/SRP132968_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193748

mkdir ./${TREEHOUSEDATA}/SRP183700 && wget -O ${TREEHOUSEDATA}/SRP183700/SRP183700_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193751

echo Downloading SRP data processed via refine.bio pipeline

mkdir ./${REFINEBIODATA}/SRP026013 && wget -O ${REFINEBIODATA}/SRP026013/SRP026013_log2TPM_plus4_HUGO.tsv https://ndownloader.figshare.com/files/27193775

mkdir ./${REFINEBIODATA}/SRP055411 && wget -O ${REFINEBIODATA}/SRP055411/SRP055411_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193781

mkdir ./${REFINEBIODATA}/SRP058841 && wget -O ${REFINEBIODATA}/SRP058841/SRP058841_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193784

mkdir ./${REFINEBIODATA}/SRP064410 && wget -O ${REFINEBIODATA}/SRP064410/SRP064410_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193790

mkdir ./${REFINEBIODATA}/SRP109549 && wget -O ${REFINEBIODATA}/SRP109549/SRP109549_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193799

mkdir ./${REFINEBIODATA}/SRP130971 && wget -O ${REFINEBIODATA}/SRP130971/SRP130971_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193802

mkdir ./${REFINEBIODATA}/SRP132968 && wget -O ${REFINEBIODATA}/SRP132968/SRP132968_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193805

mkdir ./${REFINEBIODATA}/SRP183700 && wget -O ${REFINEBIODATA}/SRP183700/SRP183700_log2TPM_plus1_HUGO.tsv https://ndownloader.figshare.com/files/27193808
