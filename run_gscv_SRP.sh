# Set data folders
DATADIR="./data/treehouse_SRP_data"
RESDIR="./results/"
MODELDIR="./models/"

python ./scripts/RF_cv.py -X ./${DATADIR}/merged_SRP_data.tsv -Y ./${DATADIR}/merged_SRP_labels.tsv -grid_search -model_out ./${MODELDIR}/rf_gscv_best_SRP.sav -results_out ./${RESDIR}/rf_gscv_results_SRP.npy -params_out ./${RESDIR}/rf_gscv_best_params_SRP.npy
