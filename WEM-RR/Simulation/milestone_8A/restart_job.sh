#!/bin/bash
#PBS -A ucichem-gibbs
#PBS -q home-gibbs
#PBS -N WE
#PBS -l nodes=1:ppn=2:gpu
#PBS -l walltime=36:00:00
#PBS -o pbs.out
#PBS -e pbs.err
#PBS -V
#PBS -M dray1@uci.edu
#PBS -m ae

#module load cuda
cd /oasis/tscc/scratch/dray1/dhiman/WEM-Testing/FKBP/weighted-ensemble-milestoning/10_trajectories/trial_1/milestone_8A

source /home/dray1/Miniconda2/etc/profile.d/conda.sh

conda activate westpa-2017.10

#---------------run.sh--------------------------------
rm -f west.log
$WEST_ROOT/bin/w_run --work-manager processes --n-workers 30 "$@" &> west.log

conda deactivate 
