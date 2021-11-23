DATA=./data/refine_bio_SRP_data/
TREEHOUSEDATA=./data/treehouse_SRP_data/
MODEL=./models/logistic_regression_model.sav
LOGISTIC_CLASSIFIER=./results/SRP/logistic_classifier/

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP055411_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP055411_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP132968_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP132968_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP183700_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP183700_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP109549_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP109549_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP130971_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP130971_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP058841_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP058841_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP064410_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP064410_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP026013_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP026013_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${TREEHOUSEDATA}SRP127360_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP127360_TPM_log2_plus_1.TH.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP055411_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP055411_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP132968_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP132968_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP064410_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP064410_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP058841_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP058841_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP130971_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP130971_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP026013_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP026013_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP132968_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP132968_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP055411_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP055411_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP109549_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP109549_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}

python ./scripts/RF_deploy.py -i ${DATA}SRP183700_log2TPM_plus1_HUGO.tsv -o ${LOGISTIC_CLASSIFIER}SRP183700_TPM_log2_plus_1.balanced_Logistic_results.tsv -model ${MODEL}
