# Set data folders
DATADIR="./data/"
RESDIR="./results/"
MODELDIR="./models/"

python ./scripts/RF_cv.py -X ./${DATADIR}/MergedData_Balanced.tsv -Y ./${DATADIR}/MergedLabels_Balanced.tsv -grid_search -model_out ./${MODELDIR}/rf_gscv_best.sav -results_out ./${RESDIR}/rf_gscv_results.npy -params_out ./${RESDIR}/rf_gscv_best_params.npy
