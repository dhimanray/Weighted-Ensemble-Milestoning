#!/bin/bash
#$ -N TEST
#$ -q pub64
#$ -pe openmp 4
#$ -m beas
#$ -R y

/data/users/dray1/NAMD_2.12_Linux-x86_64-multicore/namd2 +p4 production.conf > production.log
