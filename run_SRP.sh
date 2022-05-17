REFINEBIODATA=./data/refine_bio_SRP_data/
TREEHOUSEDATA=./data/treehouse_SRP_data/
RF_RESULTS=./results/SRP/random_forest/
MAXDEPTH=2

if [ -d "$RF_RESULTS" ]; then
  # Take action if $RF_RESULTS exists. #
  echo "${RF_RESULTS} already exists"
else
    mkdir -p $RF_RESULTS
fi

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP055411_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP055411_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP132968_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP132968_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP183700_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP183700_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP109549_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP109549_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP130971_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP130971_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP058841_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP058841_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP064410_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP064410_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP026013_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP026013_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP127360_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP127360_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP055411_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP055411_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP132968_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP132968_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP058841_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP058841_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP130971_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP130971_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP064410_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP064410_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP026013_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP026013_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP132968_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP132968_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP055411_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP055411_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP109549_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP109549_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${REFINEBIODATA}/SRP183700_log2TPM_plus1_HUGO.tsv -o ${RF_RESULTS}SRP183700_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav
