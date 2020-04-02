#!/bin/sh

INPUT_CSV_FILENAME="risk.csv"
OUTPUT_CSV_FILENAME="risk_out.csv"

python3 main.py -n $1 -i $INPUT_CSV_FILENAME -o $OUTPUT_CSV_FILENAME