#!/bin/bash
#$ -N WESTPA
#$ -q pub8i
#$ -pe openmp 4

/data/users/dray1/NAMD_2.12_Linux-x86_64-multicore/namd2 +p4 production.conf > production.log
