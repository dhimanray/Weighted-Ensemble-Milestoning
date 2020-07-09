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

cd /oasis/tscc/scratch/dray1/dhiman/WEM-Testing/FKBP/CHARMM36/WEM/trial_1/milestone_28A

source /home/dray1/Miniconda2/etc/profile.d/conda.sh

conda activate westpa-2017.10

#------------------- EQUILIBRATE --------------------------------#
cd prep/eq
/home/dray1/NAMD_2.13_Linux-x86_64-multicore-CUDA/namd2 +idlepoll +isomalloc_sync +p 4 equilibration.conf > equilibration.log
cd ../../

#-------------------- INIT.SH -----------------------------------#
# init.sh
#
# Initialize the WESTPA simulation, creating initial states (istates) and the
# main WESTPA data file, west.h5. 
#
# If you run this script after starting the simulation, the data you generated
# will be erased!
#

source env.sh

# Make sure that WESTPA is not already running.  Running two instances of 
# WESTPA on a single node/machine can cause problems.
# The following line will kill any WESTPA process that is currently running.
pkill -9 -f w_run

# Make sure that seg_logs (log files for each westpa segment), traj_segs (data
# from each trajectory segment), and istates (initial states for starting new
# trajectories) directories exist and are empty. 
rm -rf traj_segs seg_logs istates west.h5
mkdir   seg_logs traj_segs istates

# Copy over the equilibrated conformation from ./prep to bstates/bound,
# including coordinates, velocities, and box information
mkdir bstates/bound
cp prep/eq/milestone_equilibration.restart.coor bstates/bound/seg.coor
cp prep/eq/milestone_equilibration.colvars.traj  bstates/bound/seg.colvars.traj
cp prep/eq/milestone_equilibration.restart.vel  bstates/bound/seg.vel
cp prep/eq/milestone_equilibration.restart.xsc  bstates/bound/seg.xsc
cp namd_config/distance.in  bstates/bound/

# Define the arguments for the basis states (used for generating initial 
# states; in this case we only have one), and target states (used for
# knowing when to recycle trajectories). In this example, we recycle
# trajectories as they reach the bound state; we focus on sampling  
# the binding process (and not the unbinding process).

BSTATE_ARGS="--bstate-file bstates/bstates.txt"

# Initialize the simulation, creating the main WESTPA data file (west.h5)
# The "$@" lets us take any arguments that were passed to init.sh at the
# command line and pass them along to w_init.
$WEST_ROOT/bin/w_init \
  $BSTATE_ARGS $TSTATE_ARGS \
  --segs-per-state 5 \
  --work-manager=threads "$@"


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
