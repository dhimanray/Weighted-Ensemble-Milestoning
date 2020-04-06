# Weighted Ensemble Milestoning (WEM)

Weighted Ensemble Milestoning is python package based on WESTPA Toolkit. It is intended to perform Weighted Ensemle (WE) simulation in conjunction with Milestoning. I am building this as a part of my PhD research with Prof. Ioan Andricioaei at UC Irvine. The codes are written in Python 2.7 for compatibility with WESTPA which in written in Python 2.7. It will be upgraded to Python 3 when a stable version of WESTPA in Python 3 becomes available.

The code has been tested for a 1D Potential (Directory: 1d-double-well), (10+1)D Coupled potential (Directory: 11d-double-well) and Alanine dipeptide. 

Calculations have been perfeormed for simple langevin or MD, regular WE and WE combined with milestoning for all cases. In case of 1d regular milestoning calculations were also performed.

## Acknowledgements
The 1D potential codes are adapted from WESTPA tutorial files for overdamped Langevin dynamics:
https://github.com/westpa/westpa/wiki/Executable-version-of-the-Over-damped-Langevin-Dynamics

The Alanine dipeptide and (10+1)D coupled potential codes are adapted from WESTPA Tutorial page:
https://github.com/westpa/westpa/wiki/Na--Cl--Association-with-NAMD-2.12

## Walkthrough the codes

**Simple Langevin or MD:** In case of 1D potential brute force Langevin dynamics codes are in the sub-directory *simple_langevin*. For the other two cases it is in sub-directory *production*.

**Regular WE:** This is in *no_milestone* or *no_milestone_new* directory for all the tested systems.

**WEM calculations:** These are in *X_milestones* directory where X is the number of milestones. Only one milestoning configuration for each case is shown. Only the starting milestone (*milestone_0*) and one of the intermediate milestones (e.g. *milestone_1*) is shown. The rest of the milestones can be constructed following similar pattern. The starting and and the last milestone has only one adjacent milestone where the trajectories will end. For intermediate milestones (1,2, etc.) there are two milestones (one on each side) where trajectories will end. For the last milestone, the code is same as first milestone except trajectories are stopped if x<endpoint and not the other way round.

**Instructions specific to Alanine Dipeptide:** Equilibration at a given milestone is performed in the directory *prep/eq*. Configuration and structure files for NAMD are to be kept in *namd_config* directory. All scripts required for running trajectories for WE iterations are in directory *westpa_scripts*. 

**General Instructions:** WEM is run by performing the following commands in each directory corresponding to the milestones:

```
./init.sh
./run.sh 
```

When submitting jobs in a cluster using PBS script do not do ```./run.sh```. Instead paste the text inside ```run.sh``` into your PBS nodefile.

## Analysis Scripts ##
```milestone-analysis.py```: This code calculates the mean first passage times. Also prints out the transition kernel and the various intermadiate steps of the calculation. The mean first passage time between chosen milestones are given in the last line of the output.

```flux-analysis.py```: This code calculates the equilibrium probability distribution from the eigenvector of the transition kernel with eigenvalue 1.

```plot-pmf.py```: Plots the free energy profile as a function of reaction coordinate

```single-trajectory.py```: Generates long trajectory using the information of transition probability and lifetime of milestones

```plot-single-trajectory.py```: Makes plot of the long trajectory

```connecting-dots-time-correlation.py```: Calculates the time correlation function from interpolated trajectory using time averaging formula.

```milestone-analysis-reverse.py```: Calculates the Mean First Passage Time for the reverse process


## Preprint
Following is the preprint related to this project: ArXiv: https://arxiv.org/abs/1912.10650
