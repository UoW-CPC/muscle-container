#!/bin/bash
echo "**************** Retrieve input file *****************"
# Pass the path to the input file
echo "File: $1"
echo "MUSCLE starts"
python3  muscle.py -f $1