#!/bin/bash
#$ -N WESTPA
#$ -q test
#$ -pe openmp 4
#$ -m beas
#$ -R y
#$ -ckpt restart

#unset PYTHONPATH
#unset PYTHONHOME

#module load python

source ~/.bashrc

cd /pub/dray1/weighted-ensemble-milestoning/Alanine-dipeptide/weighted-ensemble

./init.sh

./run.sh

