#!/bin/bash
#PBS -A ucichem-gibbs
#PBS -q home-gibbs
#PBS -N WE
#PBS -l nodes=1:ppn=4:gpu
#PBS -l walltime=72:00:00
#PBS -o pbs.out
#PBS -e pbs.err
#PBS -V
#PBS -M dray1@uci.edu
#PBS -m a

#module load cuda
#export NAMD="/home/anupamc/NAMD_2.13b1_Linux-x86_64-multicore-CUDA"
#export LD_LIBRARY_PATH="${NAMD}/libcudart.so.9.1"

#cd /oasis/tscc/scratch/dray1/dhiman/DNA-Hoogsteen/ATATAT/production
#module load 
#/home/dray1/NAMD_2.13b2_Linux-x86_64-multicore-CUDA/namd2 +idlepoll +isomalloc_sync +p 2 production.conf > production.log

cd /oasis/tscc/scratch/dray1/dhiman/WEM-Testing/FKBP/CHARMM36/WEM/milestone_6A

source /home/dray1/Miniconda2/etc/profile.d/conda.sh

conda activate westpa-2017.10



#-------------------- RUN.SH -----------------------------------#
rm WESTPA.e*
#
## run.sh
#
## Run the weighted ensemble simulation. Make sure you ran init.sh first!
#
#
#source env.sh

rm -f west.log
$WEST_ROOT/bin/w_run --work-manager processes --n-workers 30 "$@" &> west.log

conda deactivate 
