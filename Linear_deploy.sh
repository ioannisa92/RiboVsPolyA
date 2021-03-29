DATA=./SRP_data/refinebio_pipeline/
TREEHOUSEDATA=./SRP_data/treehouse_pipeline/
MODEL=./models/linear_regression_model.sav

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP055411_log2TPM_plus1_HUGO.tsv -o ./results/SRP055411_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP132968_log2TPM_plus1_HUGO.tsv -o ./results/SRP132968_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP183700_log2TPM_plus1_HUGO.tsv -o ./results/SRP183700_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP109549_log2TPM_plus1_HUGO.tsv -o ./results/SRP109549_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP130971_log2TPM_plus1_HUGO.tsv -o ./results/SRP130971_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP058841_log2TPM_plus1_HUGO.tsv -o ./results/SRP058841_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP064410_log2TPM_plus1_HUGO.tsv -o ./results/SRP064410_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP026013_log2TPM_plus1_HUGO.tsv -o ./results/SRP026013_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP127360_log2TPM_plus1_HUGO.tsv -o ./results/SRP127360_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP055411_log2TPM_plus1_HUGO.tsv -o ./results/SRP055411_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP132968_log2TPM_plus1_HUGO.tsv -o ./results/SRP132968_TPM_log2_plus_1.TH.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP064410.log2TPM_plus1.HUGO.tsv -o ./results/SRP064410_TPM_log2_plus_1.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP058841.log2TPM_plus1.HUGO.tsv -o ./results/SRP058841_TPM_log2_plus_1.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP130971.log2TPM_plus1.HUGO.tsv -o ./results/SRP130971_TPM_log2_plus_1.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP026013.log2TPM_plus1.HUGO.tsv -o ./results/SRP026013_TPM_log2_plus_1.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP132968.log2TPM_plus1.HUGO.tsv -o ./results/SRP132968_TPM_log2_plus_1.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP055411.log2TPM_plus1.HUGO.tsv -o ./results/SRP055411_TPM_log2_plus_1.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP109549.log2TPM_plus1.HUGO.tsv -o ./results/SRP109549_TPM_log2_plus_1.balanced_Linear_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP183700.log2TPM_plus1.HUGO.tsv -o ./results/SRP183700_TPM_log2_plus_1.balanced_Linear_results.tsv -model ${MODEL}
