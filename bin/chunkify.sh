MODEL_SRC="$1"
MODEL_DST="$2"
MODEL_SPLIT_SIZE="$3"
if [ -z "${MODEL_DST}" ]
then
    MODEL_DST="$PWD/output/MODEL_CHUNKED.zip"
fi
echo "(1) Chunked model will be saved to ${MODEL_DST}"
if [ -z "${MODEL_SPLIT_SIZE}" ]
then
    MODEL_SPLIT_SIZE="30m"
fi
echo "(2) SPLIT size is ${MODEL_SPLIT_SIZE}"

if [ ! -d "${MODEL_SRC}" ]
then
    echo "MODEL NOT found. Please double check the path to the provided model"
    exit 1
fi
echo "MODEL @ ¬ ${MODEL_SRC}. Starting chunking process ... Might take a while... Please wait... "

zip -r -s ${MODEL_SPLIT_SIZE} ${MODEL_DST} ${MODEL_SRC}
