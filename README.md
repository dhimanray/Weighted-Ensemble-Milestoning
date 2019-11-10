# Weighted Ensemble Milestoning (WEM)

Weighted Ensemble Milestoning is python package based on WESTPA Toolkit. It is intended for performing Weighted Ensemle (WE) simulation in conjunction with Milestoning. I am building this as a part of my PhD project with Prof. Ioan Andricioaei at UC Irvine.

This is being tested for a 1D Potential (Directory: 1d-double-well), (10+1)D Coupled potential (Directory: 11d-double-well) and on Alanine dipeptide. 

Calculations have been perfeormed for simple langevin or MD, regular WE and WE combined with milestoning for all cases. In case of 1d regular milestoning calculations were also performed.

## Walkthrough the codes

**Simple Langevin or MD:** In cased of 1D this part is in directory *simple_langevin*. For the other cases it is in directory *production*

**Regular WE:** This is in *no_milestone* or *no_milestone_new* directory

**WEM calculations:** These are in *X_milestones* directory where X is the number of milestones. Only one milestoning configuration for each case is shown. Only the starting milestone (*milestone_0*) and one of the intermediate milestones (e.g. *milestone_1*) is shown. The rest of the milestones can be constructed following them. For the last milestone, the code is same as first milestone except trajectories are stopped if x<endpoint and not the other way round.

**Instructions specific to Alanine Dipeptide:** Equilibration at a given milestone is performed in the directory *prep/eq*. Configuration and structure files for NAMD are to be kept in *namd_config* directory. All scripts required for running trajectories for WE iterations are in directory *westpa_scripts*. 

**General Instructions:** WEM is run by performing the following commands in each directory corresponding to the milestones:

```
./init.sh
./run.sh &
```
