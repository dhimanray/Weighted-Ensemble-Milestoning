#:/bin/bash
#PBS -A ucichem-gibbs
#PBS -q home-gibbs
#PBS -N WE
#PBS -l nodes=1:ppn=1:gpu
#PBS -l walltime=24:00:00
#PBS -o pbs.out
#PBS -e pbs.err
#PBS -V
#PBS -M dray1@uci.edu
#PBS -m a

cd /oasis/tscc/scratch/dray1/dhiman/WEM-Testing/FKBP/CHARMM36/WEM/constrain-release/trial_1

for i in {6..28..2}
do
    f=milestone_${i}A
    cd $f
    cp ../combine.sh .
    ./combine.sh namd_config/ionized.psf > combine.log
    cd ..
done

#for i in 5
#do
#    f=milestone_${i}A
#    cd $f
#    cp ../combine.sh .
#    ./combine.sh namd_config/ionized.psf > combine.log
#    cd ..
#done
