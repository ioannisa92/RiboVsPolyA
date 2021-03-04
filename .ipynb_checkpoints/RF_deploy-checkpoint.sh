DATA=./SRP_data/refine_bio_SRP_data/
TREEHOUSEDATA=./SRP_data/treehouse_SRP_data/
MAXDEPTH=2

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP055411/SRP055411_log2TPM_plus1_HUGO.tsv -o ./results/SRP055411_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP132968/SRP132968_log2TPM_plus1_HUGO.tsv -o ./results/SRP132968_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP183700/SRP183700_log2TPM_plus1_HUGO.tsv -o ./results/SRP183700_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP109549/SRP109549_log2TPM_plus1_HUGO.tsv -o ./results/SRP109549_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP130971/SRP130971_log2TPM_plus1_HUGO.tsv -o ./results/SRP130971_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP058841/SRP058841_log2TPM_plus1_HUGO.tsv -o ./results/SRP058841_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP064410/SRP064410_log2TPM_plus1_HUGO.tsv -o ./results/SRP064410_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP026013/SRP026013_log2TPM_plus1_HUGO.tsv -o ./results/SRP026013_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}/SRP127360/SRP127360_log2TPM_plus1_HUGO.tsv -o ./results/SRP127360_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP055411_log2TPM_plus1_HUGO.tsv -o ./results/SRP055411_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP132968_log2TPM_plus1_HUGO.tsv -o ./results/SRP132968_TPM_log2_plus_1.TH.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP064410/SRP064410.log2TPM_plus1.HUGO.tsv -o ./results/SRP064410_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP058841/SRP058841.log2TPM_plus1.HUGO.tsv -o ./results/SRP058841_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP130971/SRP130971.log2TPM_plus1.HUGO.tsv -o ./results/SRP130971_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP026013/SRP026013.log2TPM_plus1.HUGO.tsv -o ./results/SRP026013_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP132968/SRP132968.log2TPM_plus1.HUGO.tsv -o ./results/SRP132968_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP055411/SRP055411.log2TPM_plus1.HUGO.tsv -o ./results/SRP055411_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP109549/SRP109549.log2TPM_plus1.HUGO.tsv -o ./results/SRP109549_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav

python ./scripts/RF_deploy.py -i ${DATA}SRP183700/SRP183700.log2TPM_plus1.HUGO.tsv -o ./results/SRP183700_TPM_log2_plus_1.balanced_maxdepth${MAXDEPTH}_results.tsv -model ./models/RiboVsPoly_balanced_max_depth_${MAXDEPTH}.sav


