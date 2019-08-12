#!/bin/csh
#PBS -A ucichem-gibbs
#PBS -q home-gibbs
#PBS -N ext_eq Run1
#PBS -l nodes=1:ppn=4
###PBS -l procs=12
#PBS -l walltime=4:00:00
#PBS -o pbs.out
#PBS -e pbs.err
#PBS -V
#PBS -M dray1@uci.edu
#PBS -m ae

#module load cuda
#export NAMD="/home/anupamc/NAMD_2.13b1_Linux-x86_64-multicore-CUDA"
#export LD_LIBRARY_PATH="${NAMD}/libcudart.so.9.1"

cd /oasis/tscc/scratch/dray1/dhiman/weighted-ensemble-milestoning/Alanine-dipeptide/long-production
#module load 
/home/dray1/NAMD_2.12_Linux-x86_64-multicore/namd2 +p 4 production.conf > production.log
#/home/dray1/NAMD_2.12_Linux-x86_64-multicore-CUDA/namd2 +idlepoll +isomalloc_sync +p 12 equilibriation.conf > equilibriation.log
