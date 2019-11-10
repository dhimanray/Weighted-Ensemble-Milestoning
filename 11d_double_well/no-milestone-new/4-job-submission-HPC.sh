#!/bin/bash
#$ -N WESTPA
#$ -q pub8i
#$ -pe openmp 5

conda activate westpa-2017.10


#cd /pub/dray1/weighted-ensemble-milestoning/Alanine-dipeptide/weighted-ensemble

rm WESTPA.e*
#
# run.sh
#
# Run the weighted ensemble simulation. Make sure you ran init.sh first!
#

source env.sh

rm -f west.log
$WEST_ROOT/bin/w_run --work-manager processes "$@" &> west.log

conda deactivate
