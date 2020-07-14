# Weighted Ensemble Milestoning with Restraint Release (WEM-RR)

The first implementation of WEM schem sufferes from the problem of having a single starting structure per milestone. In presence of slow orthogonal degrees of freedom it results in high variance in the results in a same system is simulated multiple times. In the WEM-RR scheme the first few (10 here) iterations are performed with a harmonic restraint on the reaction coordinate confining the system on the milestone interface. Using the weighted ensemble method 2N starting structures are generated where N is the number of trajectories per bin. Then the restraint is removed and the original simulation is initiated from this starting structures. 

## Simulation scripts specific to restraint-release

```west.cfg```: This script is the configuration file for the initial restrained iterations. Number of iteration is small (10).

```west.new.cfg```: This script is the configuration file for the original WEM simulation which will be used to calculate physical observables.

```namd_config/distance.in```: NAMD format colvars file with harmonic potential to restrain the trajectory on the milestone.
```namd_config/distance.new.in```: NAMD format colvars file with no bias on the reaction coordinate. 

It is important to note the following lines in the job submission script: ```job.sh```.
```
#--------------------- Change colvars and westpa input file -----------#

mv bstates/bound/distance.in bstates/bound/distance.old.in
mv bstates/bound/distance.new.in bstates/bound/distance.in

mv west.cfg west.old.cfg
mv west.new.cfg west.cfg

mv west.log west.old.log
```
These few lines replace the ```west.cfg``` and ```distance.in``` file with the new ones after the restrained simulation is done. 

Note: The ```west.cfg``` file in the working directory will be modified but the ```distance.in``` in the namd config directory will not be. Only the copy of the ```distance.in``` in the ```bstates\bound``` directory will be modified. At the end of the simulation no file named ```west.new.cfg``` will remain because that will become ```west.cfg```. This is done because westpa reads its input from the file named ```west.cfg```. If we want to change the settings in the middle of the simulation we need to replace the files. The rest of the ```job.sh``` script is self explanatory.

## Steps for simulating a generic system

1) Perform short equilibration in the ```prep/eq``` directory. Output name should be ```milestone_equilibration```.

2) Store all input files for simulation in ```namd_config``` directory. Make sure the name of the input restart file (.coor, .vel and .xsc) is ```parent```and the output name is ```seg```.

3) Specify the bin distribution, number of trajectories per bin, number of iterations, iteration length etc. in the ```west.cfg``` and ```west.new.cfg``` appropriately.

4) Modify ```westpa_scripts/calculatedistance.py``` to put in values of the two neighbouring milestones.

5) The job is run by submitting the ```job.sh``` file using ```qsub``` command.


## Analysis scripts

These scripts are available in Analysis directory.

```mfpt-all.py```: calculte mean first passage time (MFPT) to all other milestones starting from a given starting milestone

```mfpt-reverse-all.py```: Calculate mean first passage time from all other milestone to a given starting milestone

```mfpt-milestoning.py```: Calculate mean first passage time between two chosen milestone (also shows convergence as a function of number of matrices generated using non-reversible element exchange Monte Carlo)

```mfpt-reverse-milestoning.py```: Same as above but the MFPT is calculated for the reverse process.

```free-energy-milestoning.py```: Calculate free energy profile as a function of reaction coordinate at each milestone

```committor.py```: Calculate committor function at each milestone considering last milestone as product state

```committor-16A.py```: Calculate committor function at each milestone considering milestone at r = 16 Angstrom as product state

```runall.sh```: Convert all .ipynb analysis files into .py files and perform analysis in terminal (parallelized for 8 cores)

## Scripts for averaging and plotting

Scripts are available in the averaging and plotting directory.

```build.sh```: Generates the directory structure. Run before ```combine.py```

```combine.py```: Combine the statistics of three trials and generates an average transition kernel and lifetime vector. This program generates ```milestone-data.dat``` files in the directory of each milestone.




